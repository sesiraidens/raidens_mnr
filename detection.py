#!/usr/bin/python3
# coding: utf-8

"""
Visão "clean" mínima:
- Segue-linha: centroide ponderado em ROIs (preto/LAB)
Com logs no console e overlays no vídeo.
Sem verde, sem vermelho, sem cruzamento, sem servos/motores.
"""

import sys, time, threading
import cv2
import numpy as np

# --- compat NumPy 2.0 ---
if not hasattr(np, "int0"):
    np.int0 = np.intp

# ==== Dependências do seu ambiente (TurboPi) ====
sys.path.append('/home/pi/TurboPi/')
import Camera
import yaml_handle

# ----------------- Configurações básicas -----------------
size = (640, 480)
img_centerx = size[0] // 2

# ROIs para seguimento de linha
# (y0, y1, x0, x1, peso)
roi = [
    (240, 280, 0, 640, 0.10),
    (340, 380, 0, 640, 0.30),
    (430, 460, 0, 640, 0.60),
]

# Estrutura com faixas LAB
datalab = None

# ----------------- Utilitários -----------------
def load_config():
    """Carrega faixas LAB do YAML."""
    global datalab
    datalab = yaml_handle.get_yaml_data(yaml_handle.lab_file_path)

def getAreaMaxContour(contours):
    """Retorna (contorno_de_maior_area, area_correspondente)."""
    max_area, best = 0, None
    for c in contours:
        area = abs(cv2.contourArea(c))
        if area > max_area and area >= 5:
            max_area, best = area, c
    return best, max_area

# ----------------- Safe Camera (watchdog) -----------------
camera_lock = threading.Lock()
last_frame_ok_ts = 0.0

def reopen_camera():
    global camera
    try:
        camera.camera_close()
    except Exception:
        pass
    time.sleep(0.2)
    camera.camera_open(correction=False)

def get_frame_safe(timeout=0.8):
    global last_frame_ok_ts
    with camera_lock:
        f = camera.frame
    now = time.time()
    if f is not None:
        last_frame_ok_ts = now
        return f
    if now - last_frame_ok_ts > timeout:
        print(">>> [SAFE_CAM] Sem frames há tempo demais. Reabrindo câmera...")
        reopen_camera()
    return None

# ----------------- Pipeline de visão -----------------
def process_frame(img_bgr):
    """
    Processa um frame e retorna imagem com overlays do segue-linha.
    """
    h0, w0 = img_bgr.shape[:2]
    output = img_bgr.copy()

    frame = cv2.resize(img_bgr, size)
    frame = cv2.GaussianBlur(frame, (3, 3), 3)

    sx, sw = 0.0, 0.0
    last_box = None

    for y0, y1, x0, x1, wt in roi:
        crop = frame[y0:y1, x0:x1]
        labc = cv2.cvtColor(crop, cv2.COLOR_BGR2LAB)
        mb = cv2.inRange(
            labc,
            tuple(datalab['black']['min']),
            tuple(datalab['black']['max'])
        )
        mb = cv2.morphologyEx(
            mb, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        )
        cnts = cv2.findContours(mb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        c, a = getAreaMaxContour(cnts)
        if c is not None and a > 0:
            rect = cv2.minAreaRect(c)
            box = np.int0(cv2.boxPoints(rect))
            last_box = box.copy()

            box[:, 0] += x0
            box[:, 1] += y0
            box[:, 0] = (box[:, 0] * w0 // size[0])
            box[:, 1] = (box[:, 1] * h0 // size[1])

            cv2.drawContours(output, [box], -1, (0, 0, 255), 2)

            cx = np.mean([p[0] for p in cv2.boxPoints(rect)])
            sx += cx * wt
            sw += wt

    if sw > 0 and last_box is not None:
        cx_frame = int(sx / sw)
        cx_disp = cx_frame * w0 // size[0]
        cy_disp = int(np.mean(last_box[:, 1]))
        cv2.circle(output, (cx_disp, cy_disp), 6, (0, 255, 255), -1)
        cv2.putText(output, f"Center X: {cx_frame}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 200, 255), 2)
    else:
        cv2.putText(output, "Linha: NAO DETECTADA",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 200, 255), 2)

    return output

# ----------------- Main -----------------
if __name__ == "__main__":
    print(">>> [INIT] Carregando configuração LAB...")
    load_config()

    print(">>> [INIT] Abrindo câmera...")
    camera = Camera.Camera()
    camera.camera_open(correction=False)
    last_frame_ok_ts = time.time()

    # aquecimento da câmera
    for _ in range(15):
        f = camera.frame
        if f is None:
            time.sleep(0.03)
            continue

    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.moveWindow("frame", 100, 60)

    print(">>> [LOOP] Pressione ESC para sair.")
    try:
        while True:
            frame = get_frame_safe()
            if frame is None:
                time.sleep(0.01)
                continue

            out = process_frame(frame)
            disp = cv2.resize(out, (640, 480))
            cv2.imshow("frame", disp)

            if cv2.waitKey(1) == 27:
                break
    finally:
        camera.camera_close()
        cv2.destroyAllWindows()
        print(">>> [EXIT] Finalizado.")

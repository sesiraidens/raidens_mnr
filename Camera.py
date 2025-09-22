# Camera.py — stub para Windows usando a webcam com OpenCV
# Coloque este arquivo no MESMO diretório do seu script principal.

import cv2

class Camera:
    def __init__(self, index=0, width=640, height=480, backend=None):
        """
        index: índice da câmera (0 = webcam padrão)
        width/height: resolução desejada
        backend: backend opcional (ex.: cv2.CAP_DSHOW no Windows)
        """
        self.index = index
        self.width = int(width)
        self.height = int(height)
        self.backend = backend if backend is not None else cv2.CAP_DSHOW  # CAP_DSHOW costuma ser mais estável no Win10
        self.cap = None
        self._opened = False

    def camera_open(self, correction=False):
        """
        Mantém assinatura compatível; 'correction' é ignorado aqui.
        """
        # Abre a câmera com o backend especificado (melhor para Windows 10).
        self.cap = cv2.VideoCapture(self.index, self.backend)
        if not self.cap or not self.cap.isOpened():
            # Tenta uma segunda forma sem o backend explícito
            self.cap = cv2.VideoCapture(self.index)
        if not self.cap or not self.cap.isOpened():
            raise RuntimeError("Não foi possível abrir a webcam (index=%s)." % self.index)

        # Tenta configurar a resolução
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        self._opened = True

    def camera_close(self):
        """Fecha a câmera."""
        if self.cap is not None:
            try:
                self.cap.release()
            finally:
                self.cap = None
                self._opened = False

    @property
    def frame(self):
        """
        Lê um frame da câmera.
        Retorna None se não houver frame disponível.
        """
        if not self._opened or self.cap is None:
            return None
        ok, f = self.cap.read()
        if not ok:
            return None
        return f

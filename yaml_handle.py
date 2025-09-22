#!/usr/bin/env python3
# coding: utf-8

import os
import yaml

# Caminho padrão para o YAML de LAB (ajuste se quiser colocar em outro lugar)
lab_file_path = os.path.join(os.path.dirname(__file__), "lab_config.yaml")

# Defaults seguros caso o YAML falhe ou não tenha todas as chaves
_DEFAULT_LAB = {
    "black": {
        "min": [0, 0, 0],
        "max": [80, 255, 255],
    }
}

def _normalize_keys(d):
    """Normaliza chaves para minúsculas; mantém estrutura min/max."""
    if not isinstance(d, dict):
        return {}
    out = {}
    for k, v in d.items():
        key = str(k).lower()
        if isinstance(v, dict):
            vv = {}
            for kk, vvval in v.items():
                vv[str(kk).lower()] = vvval
            out[key] = vv
        else:
            out[key] = v
    return out

def _merge_defaults(user_cfg):
    """Mescla user_cfg sobre os defaults, garantindo min/max para 'black'."""
    cfg = _normalize_keys(user_cfg)
    merged = {}
    for color in ("black",):  # <<< importante: tupla, não string
        base = dict(_DEFAULT_LAB[color])  # cópia rasa
        user = cfg.get(color, {})
        if isinstance(user, dict):
            if "min" in user: base["min"] = list(map(int, user["min"]))
            if "max" in user: base["max"] = list(map(int, user["max"]))
        merged[color] = base
    return merged

def get_yaml_data(file_path):
    """Carrega YAML em UTF-8; se falhar, retorna defaults e loga o erro."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            print(f"[YAML_HANDLE] Aviso: {file_path} não é um mapeamento YAML válido. Usando defaults.")
            return dict(_DEFAULT_LAB)
        return _merge_defaults(data)
    except Exception as e:
        print(f"[YAML_HANDLE] Erro ao carregar {file_path}: {e}")
        print("[YAML_HANDLE] Usando faixas LAB padrão (defaults).")
        return dict(_DEFAULT_LAB)

# RAIDENS MNR

Repositorio da equipe **RAIDENS - SESI Aluminio 192** para a **MNR 2025 (Mostra Nacional de Robotica)**.

## Sobre

Sistema de visao computacional desenvolvido em **Python** com **OpenCV** para o rob competidor da **Olimpiada Brasileira de Robotica (OBR)**. O projeto foca em seguimento de linha, deteccao de cores e tomada de decisao autonoma.

## Funcionalidades

- **Seguimento de linha com PID** - Ajuste dinamico de trajetoria e velocidade
- **Deteccao de cores LAB** - Segmentacao robusta em diferentes condicoes de iluminacao
- **Reconhecimento de marcadores** - Deteccao de sinais visuais para curvas e paradas
- **Modo de resgate** - Reconhecimento de zonas e objetos
- **Calibracao via YAML** - Arquivos de configuracao para ajustes rapidos

## Estrutura

`
raidens_mnr/
├── Camera.py          # Captura e processamento de video
├── detection.py       # Deteccao de cores e marcadores
├── yaml_handle.py     # Leitura/escrita de arquivos YAML
├── lab_config.yaml    # Configuracao de calibracao LAB
└── README.md
`

## Requisitos

- Python 3.7+
- OpenCV 4.x+
- NumPy
- PyYAML

## Instalacao

`ash
git clone https://github.com/sesiraidens/raidens_mnr.git
cd raidens_mnr
pip install -r requirements.txt
`

## Uso

`ash
python Camera.py
`

## Equipe

**RAIDENS - SESI Aluminio 192**

Projeto apresentado na **Mostra Nacional de Robotica 2025**.
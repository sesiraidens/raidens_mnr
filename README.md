<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" width="80">

# RAIDENS MNR 2025

**Trabalho apresentado pela equipe RAIDENS - SESI Aluminio 192 na Mostra Nacional de Robotica 2025**

<img src="https://mnr.robocup.org.br/wp-content/uploads/2021/08/image-13.png" width="120">

</div>

---

## Sobre

Este e o repositorio do trabalho apresentado pela equipe **RAIDENS - SESI Aluminio 192** na **MNR 2025 (Mostra Nacional de Robotica)**. O projeto consiste em um sistema de visao computacional desenvolvido em **Python** com **OpenCV** para o rob competidor da **Olimpiada Brasileira de Robotica (OBR)**, com foco em seguimento de linha, deteccao de cores e tomada de decisao autonoma.

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

---

<div align="center">

**Equipe RAIDENS - SESI Aluminio 192**

MNR 2025

</div>
<div align="center" class="text-center">
<h1>RAIDENS_MNR</h1>
<p><em>Confira nossos códigos</em></p>

<img alt="last-commit" src="https://img.shields.io/github/last-commit/sesiraidens/raidens_mnr?style=flat&logo=git&logoColor=white&color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-top-language" src="https://img.shields.io/github/languages/top/sesiraidens/raidens_mnr?style=flat&color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="repo-language-count" src="https://img.shields.io/github/languages/count/sesiraidens/raidens_mnr?style=flat&color=0080ff" class="inline-block mx-1" style="margin: 0px 2px;">
<p><em>Apresentação:</em></p>
<img alt="Python" src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="OpenCV" src="https://img.shields.io/badge/OpenCV-5C3EE8.svg?style=flat&logo=OpenCV&logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
<img alt="YAML" src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" class="inline-block mx-1" style="margin: 0px 2px;">
</div>

---

## Sobre o Projeto

**RAIDENS_MNR** é o repositório oficial da equipe **RAIDENS – SESI Alumínio 192** para a **MNR 2025 (Mostra Nacional de Robótica)**.  
Ele reúne todos os códigos desenvolvidos em **Python** para o robô competidor da **OBR (Olimpíada Brasileira de Robótica)**, com foco em visão computacional, automação e tomada de decisão autônoma.

Este repositório inclui:
- Programações principais em Python utilizando OpenCV   
- Arquivos de calibração de cores (`.yml` e `.yaml`)  
- Módulos auxiliares para controle de motores, PID e sensores  
- Programação comentada de cada etapa do processo de desenvolvimento  

---

## Visão Geral

O objetivo do projeto é criar um sistema de visão computacional robusto e modular que permita ao robô:

- Seguir linhas com precisão em diferentes condições de iluminação  
- Detectar marcadores vermelhos e verdes para tomada de decisões estratégicas  
- Ler sensores e executar ações autônomas com base no ambiente  
- Entrar em modo de resgate com reconhecimento de zonas e objetos  
- Facilitar ajustes e calibrações por meio de arquivos de configuração YAML  

---

## Principais Funcionalidades

- **Segmentação de cores LAB:** detecção robusta de cores.  
- **Interface de câmera em tempo real:** captura e processamento contínuo com OpenCV.  
- **Seguimento de linha com PID:** ajuste dinâmico de trajetória e velocidade.  
- **Detecção de marcadores:** reconhecimento de sinais visuais para curvas e paradas.    

---

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.7+  
- OpenCV 4.x+  
- NumPy  
- PyYAML  
- (Opcional) Ambiente virtual gerenciado com Conda ou venv

---

## Instalação

Clone este repositório e instale as dependências:

```bash
# Clone o repositório
git clone https://github.com/sesiraidens/raidens_mnr.git

# Entre no diretório
cd raidens_mnr

# Crie o ambiente e instale dependências
conda env create -f conda.yml
conda activate raidens_mnr
```

---

## Uso

Para executar o código principal:

```bash
conda activate raidens_mnr
python main.py
```

Substitua `main.py` pelo arquivo correspondente à aplicação desejada (por exemplo, `line_follower.py`, `color_detection.py`, etc).

---

O projeto utiliza `pytest` para testes automatizados.  
Para executá-los:

```bash
pytest
```

---

## Contribuição

Este projeto é desenvolvido e mantido pela equipe **RAIDENS – SESI Alumínio 192**.  
Contribuições são bem-vindas. Para sugerir melhorias, abra uma **issue** ou envie um **pull request**.

---

## Créditos

**Equipe RAIDENS – SESI Alumínio 192**  
Projeto apresentado na **Mostra Virtual – MNR 2025**

---

<div align="center">
  <a href="#top">Voltar ao topo</a>
</div>

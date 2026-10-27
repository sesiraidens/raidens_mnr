<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="140">

# RAIDENS · MNR 2025

**Visão computacional para seguidor de linha, apresentada na Mostra Nacional de Robótica 2025**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![YAML](https://img.shields.io/badge/Configs-YAML-CB171E?style=flat-square&logo=yaml&logoColor=white)

<img src="https://mnr.robocup.org.br/wp-content/uploads/2021/08/image-13.png" alt="Mostra Nacional de Robótica" width="120">

[Sobre](#sobre) · [Como funciona](#como-funciona) · [Instalação](#instalação) · [Execução](#execução) · [Calibração](#calibração)

</div>

---

## Sobre

Este repositório guarda o trabalho que a equipe **RAIDENS** do SESI 192 Alumínio apresentou na **[MNR 2025](https://mnr.robocup.org.br/)**. É o sistema de visão do robô que a equipe usa na **Olimpíada Brasileira de Robótica (OBR)**: a câmera enxerga a pista, o código encontra a linha preta e calcula onde ela está em relação ao centro do robô.

O código foi escrito para o kit **TurboPi** (Raspberry Pi) e também roda no Windows com uma webcam comum, o que facilita testar e apresentar o projeto sem o robô.

## Como funciona

```text
câmera ──► frame BGR ──► conversão para LAB ──► máscara da cor "black"
                                                        │
           posição X da linha ◄── centroide ponderado ◄─┘
                                  em 3 faixas (ROIs)
```

1. **Segmentação em LAB.** O frame é convertido para CIELAB, que separa a luminosidade da cor. Isso deixa a detecção do preto mais estável quando a luz da arena muda.
2. **Três regiões de interesse.** A imagem é lida em três faixas horizontais, com pesos 0,1, 0,3 e 0,6. A faixa mais próxima do robô pesa mais na decisão.
3. **Centroide ponderado.** O maior contorno de cada faixa vira um ponto. A média ponderada desses pontos dá a posição X da linha, que comparada ao centro da imagem (x = 320) indica para que lado o robô precisa corrigir.
4. **Visualização.** A janela desenha a linha detectada em cada faixa, marca o centro calculado e mostra o valor de `Center X` em tempo real.

## Requisitos

- Python 3.7 ou superior
- OpenCV 4.x
- NumPy
- PyYAML

## Instalação

```bash
git clone https://github.com/sesiraidens/raidens_mnr.git
cd raidens_mnr
pip install opencv-python numpy pyyaml
```

## Execução

```bash
python detection.py
```

Pressione `Esc` para encerrar.

| Ambiente | Como a câmera é aberta |
|---|---|
| **TurboPi** | O script adiciona `/home/pi/TurboPi/` ao caminho e usa o módulo `Camera` do kit |
| **Windows** | Mantenha o `Camera.py` deste repositório na mesma pasta. Ele usa a webcam pelo backend DirectShow, com a mesma interface do kit |

## Calibração

As faixas de cor ficam em `lab_config.yaml`, no formato do OpenCV (L, A e B de 0 a 255):

```yaml
black:
  min: [  0,   0,   0 ]
  max: [ 80, 255, 255 ]
```

Mantenha a faixa de **L** larga e refine aos poucos se aparecerem falsos positivos. Para encontrar os valores na sua iluminação, use o [`raidens-lab`](https://github.com/sesiraidens/raidens-lab).

## Estrutura

| Arquivo | Papel |
|---|---|
| `detection.py` | Programa principal: ROIs, segmentação, centroide e visualização |
| `Camera.py` | Substituto da câmera do TurboPi para rodar com webcam no Windows |
| `yaml_handle.py` | Leitura do YAML com normalização de chaves e valores padrão |
| `lab_config.yaml` | Faixas de cor em LAB |

---

<div align="center">

<img src="https://sesiraidens.github.io/portifolio/assets/logo_color-aNRVU26Y.png" alt="Logo RAIDENS" width="56">

**Equipe RAIDENS** · SESI 192 Alumínio/SP

[![Email](https://img.shields.io/badge/Email-sesiraidens%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sesiraidens@gmail.com)
[![Linktree](https://img.shields.io/badge/Linktree-sesiraidens-39E06B?style=flat-square&logo=linktree&logoColor=white)](https://linktr.ee/sesiraidens)
[![GitHub](https://img.shields.io/badge/GitHub-sesiraidens-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/sesiraidens)

</div>

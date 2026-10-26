# Esquemáticos

| Archivo | Descripción |
|---|---|
| [`milo_plano_electrico.json`](milo_plano_electrico.json) | Plano completo hecho en Mesa de Cableado (rev. 1.0): 37 componentes, 137 cables |

La tabla de cableado ([`../cableado/tabla_cableado.csv`](../cableado/tabla_cableado.csv)) se genera desde este archivo con [`../herramientas/exportar_cableado.py`](../herramientas/exportar_cableado.py). La revisión del plano y los puntos pendientes están en [`../revision_plano.md`](../revision_plano.md).

## Árbol de potencia (rev. 1.0, tal como está en el plano)

```mermaid
flowchart LR
    B1["Batería 1<br/>10S2P 36 V · 158 Wh"]
    B2["Batería 2<br/>10S2P 36 V · 158 Wh"]
    BUS(("Bus 36 V<br/>(baterías en paralelo)"))
    HB["Placa hoverboard<br/>FOC EFeru"]
    RUEDAS["2× rueda BLDC 6.5''<br/>~350 W c/u"]
    C24["Conversor 42→24 V<br/>UENPO 20 A"]
    TB["7× TB6600<br/>+ 4× NEMA 23 · 3× NEMA 17"]
    C12["Conversor 24→12 V<br/>Kuongshun 20 A"]
    C66["Conversor 24→6.6 V<br/>Kuongshun 8 A"]
    SERVO["Servo LF-20MG"]
    JET["Jetson Orin Nano"]
    HUB["Hub USB 3.0 7 puertos"]
    USB5["Periféricos 5 V USB<br/>LiDAR · IMU · WonderMV · USB-TTL<br/>monitor · GX Touch · hub MST"]
    MEGA["Arduino Mega<br/>(alimentado por USB)"]

    B1 --> BUS
    B2 --> BUS
    BUS --> HB --> RUEDAS
    BUS --> C24
    C24 --> TB
    C24 --> C12
    C24 --> C66 --> SERVO
    C12 --> JET
    C12 --> HUB --> USB5
    JET -- USB --> MEGA
    JET -- USB --> GEM["Orbbec Gemini Plus"]
```

## Señales de control

| Desde | Hacia | Interfaz |
|---|---|---|
| Jetson | Arduino Mega | USB |
| Jetson → hub USB → USB-TTL | Placa hoverboard | UART |
| Arduino Mega | 7× TB6600 | STEP (D2–D8), DIR (D22–D28), EN (D30–D36), cátodo común a GND |
| Arduino Mega | Servo | PWM D9 |
| Arduino Mega | MPU-9250 | I²C (D20/D21) |
| Seta de emergencia (2 NC) | Jetson pin 7 y Mega D18 | Entradas digitales |
| Jetson DisplayPort → hub MST | Monitor 11.6" y GX Touch 50 | HDMI |

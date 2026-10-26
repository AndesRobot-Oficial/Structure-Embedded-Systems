# Cableado — plano eléctrico rev. 1.0

Lista de los **137 cables** de la base de MILO, agrupados por circuito. Cada cable lleva una etiqueta física con su ID (C001…C137).

Fuente: mapa de conexiones de ReWire ([`../esquematicos/milo_plano_electrico.json`](../esquematicos/milo_plano_electrico.json)). Los datos también están en [`tabla_cableado.csv`](tabla_cableado.csv) para filtrar en una planilla. El árbol de potencia está en [`../esquematicos/README.md`](../esquematicos/README.md) y los puntos pendientes en [`../revision_plano.md`](../revision_plano.md).

## Resumen

| Circuito | Cables |
|---|:-:|
| [Distribución de potencia](#1-distribución-de-potencia) | 35 |
| [Tracción: placa hoverboard y ruedas](#2-tracción-placa-hoverboard-y-ruedas) | 8 |
| [Motores paso a paso](#3-motores-paso-a-paso) | 28 |
| [Control de drivers TB6600](#4-control-de-drivers-tb6600) | 42 |
| [Comunicación y periféricos del Mega](#5-comunicación-y-periféricos-del-mega) | 7 |
| [Parada de emergencia](#6-parada-de-emergencia) | 4 |
| [USB y video](#7-usb-y-video) | 13 |
| **Total** | **137** |

### Cable por calibre

| Calibre | Cables | Uso |
|---|:-:|---|
| 12 AWG | 4 | Bus de batería 36 V |
| 14 AWG | 6 | Fases de las ruedas BLDC |
| 16 AWG | 18 | Salida 24 V (TB6600 y conversores) |
| 18 AWG | 38 | 12 V, 6,6 V, 5 V y bobinas de motores paso a paso |
| 24 AWG | 58 | Señales de control |
| Cable USB | 10 | Datos y alimentación USB |
| Cable de vídeo | 3 | DisplayPort / HDMI |

> ⚠ **C108–C111** (batería → conversor 42→24 V y placa hoverboard) están en 24 AWG en el plano, pero llevan corriente de potencia. Ver el punto 3 de la [revisión del plano](../revision_plano.md).

### Código de colores

| Color | Uso |
|---|---|
| Rojo | Positivo de alimentación |
| Negro | GND / negativo |
| Amarillo | STEP, SCL, UART RX, E-STOP |
| Verde | DIR, UART TX |
| Naranjo | EN, señal del servo |
| Azul | SDA, USB |
| Gris | Video, Hall, botón |
| Rojo / Negro / Verde / Azul | Bobinas B+ / A+ / A− / B− de los motores paso a paso |
| Amarillo / Azul / Verde | Fases A / B / C de las ruedas |

## 1. Distribución de potencia

Baterías, conversores DC-DC y alimentación de cada equipo.

| ID | Desde | Pin | Hacia | Pin | Señal | Color | Calibre |
|---|---|---|---|---|---|---|---|
| C001 | Batería 2 | − | Conversor 42 V → 24 V | IN − | GND | Negro | 12 AWG |
| C002 | Batería 1 | + | Conversor 42 V → 24 V | IN + | +36 V | Rojo | 12 AWG |
| C003 | Conversor 42 V → 24 V | OUT − | Conversor 24 V → 12 V | IN − | GND | Negro | 16 AWG |
| C004 | Conversor 42 V → 24 V | OUT + 24V | Conversor 24 V → 12 V | IN + | +24 V | Rojo | 16 AWG |
| C005 | Conversor 42 V → 24 V | OUT − | Conversor 24 V → 6.6 V | IN − | GND | Negro | 16 AWG |
| C006 | Conversor 42 V → 24 V | OUT + 24V | Conversor 24 V → 6.6 V | IN + | +24 V | Rojo | 16 AWG |
| C024 | Conversor 24 V → 12 V | OUT − | Hub USB 3.0 alimentado | GND − | GND | Negro | 18 AWG |
| C025 | Conversor 24 V → 12 V | OUT + 12V | Hub USB 3.0 alimentado | DC IN + | +12 V | Rojo | 18 AWG |
| C026 | Conversor 24 V → 12 V | OUT − | Jetson Orin Nano | GND − | GND | Negro | 18 AWG |
| C027 | Conversor 24 V → 12 V | OUT + 12V | Jetson Orin Nano | DC IN + | +12 V | Rojo | 18 AWG |
| C029 | Arduino Mega 2560 | GND | IMU MPU-9250 | GND | GND | Negro | 18 AWG |
| C032 | Arduino Mega 2560 | 5V | IMU MPU-9250 | VCC | 5V | Rojo | 18 AWG |
| C036 | Conversor 42 V → 24 V | OUT − | TB6600 #1 | GND − | GND | Negro | 16 AWG |
| C037 | Conversor 42 V → 24 V | OUT + 24V | TB6600 #1 | VCC + | +24 V | Rojo | 16 AWG |
| C038 | Conversor 42 V → 24 V | OUT − | TB6600 #2 | GND − | GND | Negro | 16 AWG |
| C039 | Conversor 42 V → 24 V | OUT + 24V | TB6600 #2 | VCC + | +24 V | Rojo | 16 AWG |
| C040 | Conversor 42 V → 24 V | OUT − | TB6600 #3 | GND − | GND | Negro | 16 AWG |
| C041 | Conversor 42 V → 24 V | OUT + 24V | TB6600 #3 | VCC + | +24 V | Rojo | 16 AWG |
| C042 | Conversor 42 V → 24 V | OUT − | TB6600 #4 | GND − | GND | Negro | 16 AWG |
| C043 | Conversor 42 V → 24 V | OUT + 24V | TB6600 #4 | VCC + | +24 V | Rojo | 16 AWG |
| C044 | Conversor 42 V → 24 V | OUT − | TB6600 #5 | GND − | GND | Negro | 16 AWG |
| C045 | Conversor 42 V → 24 V | OUT + 24V | TB6600 #5 | VCC + | +24 V | Rojo | 16 AWG |
| C046 | Conversor 42 V → 24 V | OUT − | TB6600 #6 | GND − | GND | Negro | 16 AWG |
| C047 | Conversor 42 V → 24 V | OUT + 24V | TB6600 #6 | VCC + | +24 V | Rojo | 16 AWG |
| C048 | Conversor 42 V → 24 V | OUT − | TB6600 #7 | GND − | GND | Negro | 16 AWG |
| C049 | Conversor 42 V → 24 V | OUT + 24V | TB6600 #7 | VCC + | +24 V | Rojo | 16 AWG |
| C051 | Conversor 24 V → 6.6 V | OUT − | Servo Power HD LF-20MG | GND (marrón) | GND | Negro | 18 AWG |
| C052 | Conversor 24 V → 6.6 V | OUT + 6.6V | Servo Power HD LF-20MG | V+ (rojo) | +6,6 V | Rojo | 18 AWG |
| C053 | Arduino Mega 2560 | GND | Servo Power HD LF-20MG | GND (marrón) | GND ref | Negro | 18 AWG |
| **C108** ⚠ | Batería 2 | + | Conversor 42 V → 24 V | IN + | +36 V | Rojo | 24 AWG |
| **C109** ⚠ | Batería 1 | − | Conversor 42 V → 24 V | IN − | GND | Negro | 24 AWG |
| **C110** ⚠ | Batería 1 | + | Placa hoverboard | BAT + | +36 V | Rojo | 24 AWG |
| **C111** ⚠ | Batería 1 | − | Placa hoverboard | BAT − | GND | Negro | 24 AWG |
| C132 | Batería 2 | + | Placa hoverboard | BAT + | +36 V | Rojo | 12 AWG |
| C133 | Batería 2 | − | Placa hoverboard | BAT − | GND | Negro | 12 AWG |

## 2. Tracción: placa hoverboard y ruedas

Fases y sensores Hall de los motores BLDC.

| ID | Desde | Pin | Hacia | Pin | Señal | Color | Calibre |
|---|---|---|---|---|---|---|---|
| C100 | Placa hoverboard | MOTOR IZQ A | Rueda izquierda | FASE A | Fase A | Amarillo | 14 AWG |
| C101 | Placa hoverboard | MOTOR IZQ B | Rueda izquierda | FASE B | Fase B | Azul | 14 AWG |
| C102 | Placa hoverboard | MOTOR IZQ C | Rueda izquierda | FASE C | Fase C | Verde | 14 AWG |
| C103 | Placa hoverboard | HALL IZQ | Rueda izquierda | HALL (5 hilos) | Hall | Gris | 24 AWG |
| C104 | Placa hoverboard | MOTOR DER A | Rueda derecha | FASE A | Fase A | Amarillo | 14 AWG |
| C105 | Placa hoverboard | MOTOR DER B | Rueda derecha | FASE B | Fase B | Azul | 14 AWG |
| C106 | Placa hoverboard | MOTOR DER C | Rueda derecha | FASE C | Fase C | Verde | 14 AWG |
| C107 | Placa hoverboard | HALL DER | Rueda derecha | HALL (5 hilos) | Hall | Gris | 24 AWG |

## 3. Motores paso a paso

Bobinas entre cada TB6600 y su motor.

| ID | Desde | Pin | Hacia | Pin | Señal | Color | Calibre |
|---|---|---|---|---|---|---|---|
| C062 | TB6600 #1 | A− | NEMA 23 1.26 N·m #1 | A− | Bobina A− | Verde | 18 AWG |
| C063 | TB6600 #1 | A+ | NEMA 23 1.26 N·m #1 | A+ | Bobina A+ | Negro | 18 AWG |
| C064 | TB6600 #1 | B− | NEMA 23 1.26 N·m #1 | B− | Bobina B− | Azul | 18 AWG |
| C065 | TB6600 #1 | B+ | NEMA 23 1.26 N·m #1 | B+ | Bobina B+ | Rojo | 18 AWG |
| C066 | TB6600 #2 | A− | NEMA 23 1.26 N·m #2 | A− | Bobina A− | Verde | 18 AWG |
| C067 | TB6600 #2 | A+ | NEMA 23 1.26 N·m #2 | A+ | Bobina A+ | Negro | 18 AWG |
| C068 | TB6600 #2 | B− | NEMA 23 1.26 N·m #2 | B− | Bobina B− | Azul | 18 AWG |
| C069 | TB6600 #2 | B+ | NEMA 23 1.26 N·m #2 | B+ | Bobina B+ | Rojo | 18 AWG |
| C070 | TB6600 #3 | A− | NEMA 23 1.26 N·m #3 | A− | Bobina A− | Verde | 18 AWG |
| C071 | TB6600 #3 | A+ | NEMA 23 1.26 N·m #3 | A+ | Bobina A+ | Negro | 18 AWG |
| C072 | TB6600 #3 | B− | NEMA 23 1.26 N·m #3 | B− | Bobina B− | Azul | 18 AWG |
| C073 | TB6600 #3 | B+ | NEMA 23 1.26 N·m #3 | B+ | Bobina B+ | Rojo | 18 AWG |
| C074 | TB6600 #4 | A− | NEMA 23 2.9 N·m | A− | Bobina A− | Verde | 18 AWG |
| C075 | TB6600 #4 | A+ | NEMA 23 2.9 N·m | A+ | Bobina A+ | Negro | 18 AWG |
| C076 | TB6600 #4 | B− | NEMA 23 2.9 N·m | B− | Bobina B− | Azul | 18 AWG |
| C077 | TB6600 #4 | B+ | NEMA 23 2.9 N·m | B+ | Bobina B+ | Rojo | 18 AWG |
| C078 | TB6600 #5 | A− | NEMA 17 #1 | A− | Bobina A− | Verde | 18 AWG |
| C079 | TB6600 #5 | A+ | NEMA 17 #1 | A+ | Bobina A+ | Negro | 18 AWG |
| C080 | TB6600 #5 | B− | NEMA 17 #1 | B− | Bobina B− | Azul | 18 AWG |
| C081 | TB6600 #5 | B+ | NEMA 17 #1 | B+ | Bobina B+ | Rojo | 18 AWG |
| C082 | TB6600 #6 | A− | NEMA 17 #2 | A− | Bobina A− | Verde | 18 AWG |
| C083 | TB6600 #6 | A+ | NEMA 17 #2 | A+ | Bobina A+ | Negro | 18 AWG |
| C084 | TB6600 #6 | B− | NEMA 17 #2 | B− | Bobina B− | Azul | 18 AWG |
| C085 | TB6600 #6 | B+ | NEMA 17 #2 | B+ | Bobina B+ | Rojo | 18 AWG |
| C086 | TB6600 #7 | A− | NEMA 17 #3 | A− | Bobina A− | Verde | 18 AWG |
| C087 | TB6600 #7 | A+ | NEMA 17 #3 | A+ | Bobina A+ | Negro | 18 AWG |
| C088 | TB6600 #7 | B− | NEMA 17 #3 | B− | Bobina B− | Azul | 18 AWG |
| C089 | TB6600 #7 | B+ | NEMA 17 #3 | B+ | Bobina B+ | Rojo | 18 AWG |

## 4. Control de drivers TB6600

Señales STEP, DIR y EN desde el Arduino Mega, con cátodo común a GND.

| ID | Desde | Pin | Hacia | Pin | Señal | Color | Calibre |
|---|---|---|---|---|---|---|---|
| C007 | Arduino Mega 2560 | DIR1 (D22) | TB6600 #1 | DIR+ | DIR1 | Verde | 24 AWG |
| C008 | Arduino Mega 2560 | DIR2 (D23) | TB6600 #2 | DIR+ | DIR2 | Verde | 24 AWG |
| C009 | Arduino Mega 2560 | DIR3 (D24) | TB6600 #3 | DIR+ | DIR3 | Verde | 24 AWG |
| C010 | Arduino Mega 2560 | DIR4 (D25) | TB6600 #4 | DIR+ | DIR4 | Verde | 24 AWG |
| C011 | Arduino Mega 2560 | DIR5 (D26) | TB6600 #5 | DIR+ | DIR5 | Verde | 24 AWG |
| C012 | Arduino Mega 2560 | DIR6 (D27) | TB6600 #6 | DIR+ | DIR6 | Verde | 24 AWG |
| C013 | Arduino Mega 2560 | DIR7 (D28) | TB6600 #7 | DIR+ | DIR7 | Verde | 24 AWG |
| C016 | Arduino Mega 2560 | EN1 (D30) | TB6600 #1 | ENA+ | EN1 | Naranjo | 24 AWG |
| C017 | Arduino Mega 2560 | EN2 (D31) | TB6600 #2 | ENA+ | EN2 | Naranjo | 24 AWG |
| C018 | Arduino Mega 2560 | EN3 (D32) | TB6600 #3 | ENA+ | EN3 | Naranjo | 24 AWG |
| C019 | Arduino Mega 2560 | EN4 (D33) | TB6600 #4 | ENA+ | EN4 | Naranjo | 24 AWG |
| C020 | Arduino Mega 2560 | EN5 (D34) | TB6600 #5 | ENA+ | EN5 | Naranjo | 24 AWG |
| C021 | Arduino Mega 2560 | EN6 (D35) | TB6600 #6 | ENA+ | EN6 | Naranjo | 24 AWG |
| C022 | Arduino Mega 2560 | EN7 (D36) | TB6600 #7 | ENA+ | EN7 | Naranjo | 24 AWG |
| C050 | Arduino Mega 2560 | GND (señales motores) | TB6600 #1 | PUL− | GND señal | Negro | 24 AWG |
| C055 | Arduino Mega 2560 | STEP1 (D2) | TB6600 #1 | PUL+ | STEP1 | Amarillo | 24 AWG |
| C056 | Arduino Mega 2560 | STEP2 (D3) | TB6600 #2 | PUL+ | STEP2 | Amarillo | 24 AWG |
| C057 | Arduino Mega 2560 | STEP3 (D4) | TB6600 #3 | PUL+ | STEP3 | Amarillo | 24 AWG |
| C058 | Arduino Mega 2560 | STEP4 (D5) | TB6600 #4 | PUL+ | STEP4 | Amarillo | 24 AWG |
| C059 | Arduino Mega 2560 | STEP5 (D6) | TB6600 #5 | PUL+ | STEP5 | Amarillo | 24 AWG |
| C060 | Arduino Mega 2560 | STEP6 (D7) | TB6600 #6 | PUL+ | STEP6 | Amarillo | 24 AWG |
| C061 | Arduino Mega 2560 | STEP7 (D8) | TB6600 #7 | PUL+ | STEP7 | Amarillo | 24 AWG |
| C112 | Arduino Mega 2560 | GND (señales motores) | TB6600 #1 | DIR− | GND señal | Negro | 24 AWG |
| C113 | Arduino Mega 2560 | GND (señales motores) | TB6600 #1 | ENA− | GND señal | Negro | 24 AWG |
| C114 | Arduino Mega 2560 | GND (señales motores) | TB6600 #2 | PUL− | GND señal | Negro | 24 AWG |
| C115 | Arduino Mega 2560 | GND (señales motores) | TB6600 #2 | DIR− | GND señal | Negro | 24 AWG |
| C116 | Arduino Mega 2560 | GND (señales motores) | TB6600 #2 | ENA− | GND señal | Negro | 24 AWG |
| C117 | Arduino Mega 2560 | GND (señales motores) | TB6600 #3 | PUL− | GND señal | Negro | 24 AWG |
| C118 | Arduino Mega 2560 | GND (señales motores) | TB6600 #3 | DIR− | GND señal | Negro | 24 AWG |
| C119 | Arduino Mega 2560 | GND (señales motores) | TB6600 #3 | ENA− | GND señal | Negro | 24 AWG |
| C120 | Arduino Mega 2560 | GND (señales motores) | TB6600 #4 | PUL− | GND señal | Negro | 24 AWG |
| C121 | Arduino Mega 2560 | GND (señales motores) | TB6600 #4 | DIR− | GND señal | Negro | 24 AWG |
| C122 | Arduino Mega 2560 | GND (señales motores) | TB6600 #4 | ENA− | GND señal | Negro | 24 AWG |
| C123 | Arduino Mega 2560 | GND (señales motores) | TB6600 #5 | PUL− | GND señal | Negro | 24 AWG |
| C124 | Arduino Mega 2560 | GND (señales motores) | TB6600 #5 | DIR− | GND señal | Negro | 24 AWG |
| C125 | Arduino Mega 2560 | GND (señales motores) | TB6600 #5 | ENA− | GND señal | Negro | 24 AWG |
| C126 | Arduino Mega 2560 | GND (señales motores) | TB6600 #6 | PUL− | GND señal | Negro | 24 AWG |
| C127 | Arduino Mega 2560 | GND (señales motores) | TB6600 #6 | DIR− | GND señal | Negro | 24 AWG |
| C128 | Arduino Mega 2560 | GND (señales motores) | TB6600 #6 | ENA− | GND señal | Negro | 24 AWG |
| C129 | Arduino Mega 2560 | GND (señales motores) | TB6600 #7 | PUL− | GND señal | Negro | 24 AWG |
| C130 | Arduino Mega 2560 | GND (señales motores) | TB6600 #7 | DIR− | GND señal | Negro | 24 AWG |
| C131 | Arduino Mega 2560 | GND (señales motores) | TB6600 #7 | ENA− | GND señal | Negro | 24 AWG |

## 5. Comunicación y periféricos del Mega

UART de la placa hoverboard, botón de encendido, IMU MPU-9250 y servo.

| ID | Desde | Pin | Hacia | Pin | Señal | Color | Calibre |
|---|---|---|---|---|---|---|---|
| C023 | Pulsador hoverboard | BOTÓN | Placa hoverboard | BOTÓN ON | Botón ON | Gris | 24 AWG |
| C030 | Arduino Mega 2560 | SCL (D21) | IMU MPU-9250 | SCL | SCL | Amarillo | 24 AWG |
| C031 | Arduino Mega 2560 | SDA (D20) | IMU MPU-9250 | SDA | SDA | Azul | 24 AWG |
| C054 | Arduino Mega 2560 | SERVO (D9) | Servo Power HD LF-20MG | SEÑAL (naranja) | SERVO | Naranjo | 24 AWG |
| C090 | Placa hoverboard | UART GND | USB a TTL | GND | GND | Negro | 18 AWG |
| C091 | Placa hoverboard | UART TX | USB a TTL | RXD | UART TX | Verde | 24 AWG |
| C092 | Placa hoverboard | UART RX | USB a TTL | TXD | UART RX | Amarillo | 24 AWG |

## 6. Parada de emergencia

Dos contactos NC, uno hacia el Jetson y otro hacia el Mega.

| ID | Desde | Pin | Hacia | Pin | Señal | Color | Calibre |
|---|---|---|---|---|---|---|---|
| C134 | Jetson Orin Nano | GND header (pin 6) | Seta de emergencia | COM 1 | E-STOP | Negro | 24 AWG |
| C135 | Seta de emergencia | SALIDA 1 (NC) | Jetson Orin Nano | GPIO E-STOP (pin 7) | E-STOP | Amarillo | 24 AWG |
| C136 | Arduino Mega 2560 | GND | Seta de emergencia | COM 2 | E-STOP | Negro | 24 AWG |
| C137 | Seta de emergencia | SALIDA 2 (NC) | Arduino Mega 2560 | E-STOP (D18) | E-STOP | Amarillo | 24 AWG |

## 7. USB y video

Cables de datos USB, DisplayPort y HDMI.

| ID | Desde | Pin | Hacia | Pin | Señal | Color | Calibre |
|---|---|---|---|---|---|---|---|
| C014 | Hub DisplayPort MST | HDMI 1 | Monitor MUCAI N116A | HDMI IN | HDMI | Gris | Cable de vídeo |
| C015 | Jetson Orin Nano | DisplayPort | Hub DisplayPort MST | DP IN | DisplayPort | Gris | Cable de vídeo |
| C028 | Hub USB 3.0 alimentado | Puerto 1 | Monitor MUCAI N116A | USB-C 5V | USB 5V | Azul | Cable USB |
| C033 | Hub USB 3.0 alimentado | Puerto 2 | Hub DisplayPort MST | USB 5V | USB 5V | Azul | Cable USB |
| C034 | Hub DisplayPort MST | HDMI 2 | Victron GX Touch 50 | HDMI IN | HDMI | Gris | Cable de vídeo |
| C035 | Hub USB 3.0 alimentado | Puerto 6 | Hiwonder WonderMV | USB Type-C | USB | Azul | Cable USB |
| C093 | Jetson Orin Nano | USB-A 2 | Orbbec Gemini Plus | USB-C 3.0 | USB 3.0 | Azul | Cable USB |
| C094 | Jetson Orin Nano | USB-A 1 | Hub USB 3.0 alimentado | USB entrada (a Jetson) | USB 3.0 | Azul | Cable USB |
| C095 | Hub USB 3.0 alimentado | Puerto 3 | IMU HFI-B9 | USB | USB | Azul | Cable USB |
| C096 | Hub USB 3.0 alimentado | Puerto 5 | RPLIDAR C1 | USB (adaptador) | USB | Azul | Cable USB |
| C097 | Jetson Orin Nano | USB-A 3 | Arduino Mega 2560 | USB-B | USB | Azul | Cable USB |
| C098 | USB a TTL | USB | Hub USB 3.0 alimentado | Puerto 7 | USB | Azul | Cable USB |
| C099 | Hub USB 3.0 alimentado | Puerto 4 | Victron GX Touch 50 | USB (táctil + 5V) | USB | Azul | Cable USB |

## Largos

Los largos se miden en el robot y se anotan en la columna `largo_mm` de [`tabla_cableado.csv`](tabla_cableado.csv).

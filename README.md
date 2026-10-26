# MILO — Estructura y Sistemas Embebidos

Repositorio del equipo de **base** de [AndesRobot](https://github.com/AndesRobot-Oficial) para el robot **MILO** (RoboCup@Home 2027).
Contiene el modelo CAD, el sistema eléctrico de la base y el modelo URDF para ROS 2.

## Especificaciones

| Parámetro | Valor |
|---|---|
| Dimensiones (L × A × H) | 50 × 50 × 175 cm (provisorio) |
| Peso | ~31 kg, estimación preliminar |
| Tipo de tracción | Diferencial, 2 motores BLDC de hoverboard 6,5" (control FOC) |
| Velocidad máxima | 6 km/h |
| Batería | 2× Li-ion 10S2P 36 V · 4,4 Ah · 158 Wh (316 Wh en total) |
| Autonomía estimada | ~1,4 h, estimación preliminar (ver [presupuesto de potencia](electrica/presupuesto_potencia.csv)) |
| Computador principal | NVIDIA Jetson Orin Nano Dev Kit + Arduino Mega 2560 |
| Sensores | RPLIDAR C1, Orbbec Gemini Plus, IMU HFI-B9, IMU MPU-9250, Hiwonder WonderMV |
| Pantallas | Monitor MUCAI N116A 11,6" y Victron GX Touch 50 (no necesariamente serán estos modelos) |
| Software | ROS 2 Humble · Ubuntu 22.04 |
| CAD | Autodesk Fusion 360 |

## Estado actual

| Área | Estado |
|---|---|
| Diseño 3D | ✅ Listo ([modelo CAD](cad/README.md)) |
| Plano eléctrico | 🟡 Rev. 2.0 lista, pendientes las medidas de seguridad ([revisión](electrica/revision_plano.md)) |
| URDF | 🟡 Modelo del CAD con masas estimadas |
| BOM | 🟡 Componentes eléctricos listos; falta perfilería y tornillería |
| Fabricación | 🟡 Pendiente la carcasa exterior |

🔲 Pendiente · 🟡 En progreso · ✅ Listo

## Estructura del repositorio

```
.
├── bom/              # Lista de componentes
├── cad/              # Archivo CAD del robot
├── electrica/        # Diagrama de conexiones
└── milo_description/ # URDF del robot con masas calculadas
```

## Uso rápido del URDF

Requiere ROS 2 Humble.

```bash
cd ~/ros2_ws/src
git clone https://github.com/AndesRobot-Oficial/Structure-Embedded-Systems_MILO.git
cd ~/ros2_ws
colcon build --packages-select andesrobot_description
source install/setup.bash
ros2 launch andesrobot_description display.launch.py
```

## Contacto

Base de MILO: [@Dlpez](https://github.com/Dlpez)

# MILO — Estructura y Sistemas Embebidos

Repositorio del equipo de **base** de [AndesRobot](https://github.com/AndesRobot-Oficial) para el robot **MILO** (RoboCup@Home 2027).
Contiene el sistema eléctrico de la base, el modelo URDF para ROS 2 y los cálculos de diseño.

## Especificaciones

| Parámetro | Valor |
|---|---|
| Dimensiones (L × A × H) | 50 × 50 × 175 cm (provisorio) |
| Peso | ~31 kg, estimación preliminar (ver [masas](docs/calculos/masas.md)) |
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
| Diseño 3D | ✅ Listo |
| Plano eléctrico | 🟡 Rev. 2.0 lista, pendientes las medidas de seguridad ([revisión](electrica/revision_plano.md)) |
| URDF | 🟡 Modelo del CAD con masas estimadas |
| BOM | 🟡 Componentes eléctricos listos; falta perfilería y tornillería |
| Fabricación | 🟡 Pendiente la carcasa exterior |

🔲 Pendiente · 🟡 En progreso · ✅ Listo

## Estructura del repositorio

```
.
├── electrica/
│   ├── esquematicos/ # Plano eléctrico (mapa de conexiones de ReWire)
│   ├── cableado/     # Lista de cableado
│   ├── presupuesto_potencia.csv
│   └── revision_plano.md
├── milo_description/ # Paquete ROS 2 andesrobot_description (URDF/xacro + mallas)
├── bom/              # Lista de materiales
└── docs/
    ├── calculos/     # Masas, centro de masa y vuelco
    ├── decisiones.md # Registro de decisiones de diseño
    └── checklist_competencia.md
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

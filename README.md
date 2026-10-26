# MILO — Estructura y Sistemas Embebidos

Repositorio del equipo de **base** de [AndesRobot](https://github.com/AndesRobot-Oficial) para el robot **MILO** (RoboCup@Home 2027).
Contiene el diseño mecánico de la base, el sistema eléctrico y el modelo URDF para ROS 2.

<!-- Agregar foto o render de MILO aquí: ![MILO](docs/fotos/milo.jpg) -->

## Especificaciones

| Parámetro | Valor |
|---|---|
| Dimensiones (L × A × H) | 50 × 50 × 175 cm (provisorio; el brazo no cambia estas medidas) |
| Peso | _por definir_ |
| Tipo de tracción | Diferencial, 2 motores BLDC de hoverboard 6,5" (control FOC) |
| Velocidad máxima | 6 km/h |
| Carga en la punta del brazo | 2 kg teóricos a máxima extensión (sin comprobar) |
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
| URDF | 🟡 Plantilla inicial (medidas provisorias) |
| BOM | 🟡 Componentes eléctricos listos; falta perfilería y tornillería |
| Fabricación | 🟡 Pendiente la carcasa exterior |

🔲 Pendiente · 🟡 En progreso · ✅ Listo

## Brazo

<!-- Pendiente: información del brazo, se agrega cuando su repositorio tenga main. -->

_Por completar._

La interfaz entre la base y el brazo está en [`interfaz_brazo/`](interfaz_brazo/README.md).

## Estructura del repositorio

```
.
├── mecanica/
│   ├── cad/          # Archivos fuente de Fusion 360
│   ├── step/         # Exportaciones STEP (abren en cualquier CAD)
│   ├── stl/          # Piezas para impresión 3D + parámetros de impresión
│   ├── dxf/          # Piezas para corte láser / CNC
│   └── planos/       # Planos de fabricación en PDF
├── electrica/
│   ├── esquematicos/ # Esquemático fuente + PDF
│   ├── cableado/     # Diagrama y tabla de cableado
│   ├── pcb/          # Diseños de PCB y Gerbers
│   ├── herramientas/ # Script que genera la tabla de cableado
│   ├── presupuesto_potencia.csv
│   └── revision_plano.md
├── milo_description/ # Paquete ROS 2 con el URDF/xacro
├── interfaz_brazo/   # Acuerdo de interfaz con el equipo del brazo
├── bom/              # Lista de materiales
└── docs/
    ├── calculos/     # Torque, carga, centro de masa, FEA
    ├── ensamblaje/   # Guía de ensamblaje
    ├── datasheets/   # Hojas de datos o links
    ├── fotos/
    ├── decisiones.md # Registro de decisiones de diseño
    └── checklist_competencia.md
```

## Uso rápido del URDF

Requiere ROS 2 Humble.

```bash
cd ~/ros2_ws/src
git clone https://github.com/AndesRobot-Oficial/Structure-Embedded-Systems_MILO.git
cd ~/ros2_ws
colcon build --packages-select milo_description
source install/setup.bash
ros2 launch milo_description display.launch.py
```

## Cómo contribuir

1. No subas cambios directo a `main`: crea una rama nueva al subir los archivos.
2. Sube el archivo fuente **y** su exportación (por ejemplo, el `.f3d` de Fusion 360 y su `.step`).
3. Si cambias algo que afecta al brazo, actualiza [`interfaz_brazo/`](interfaz_brazo/README.md).
4. Anota los cambios importantes en [`CHANGELOG.md`](CHANGELOG.md) y las decisiones en [`docs/decisiones.md`](docs/decisiones.md).
5. Abre un Pull Request hacia `main`.

## Contacto

Base de MILO: [@Dlpez](https://github.com/Dlpez)

# MILO — Estructura y Sistemas Embebidos

Repositorio del equipo de **base** de [AndesRobot](https://github.com/AndesRobot-Oficial) para el robot **MILO** (RoboCup@Home 2027).
Contiene el diseño mecánico de la base, el sistema eléctrico y el modelo URDF para ROS 2.



<!-- Agregar foto o render de MILO aquí: ![MILO](docs/fotos/milo.jpg) -->

## Especificaciones

| Parámetro | Valor |
|---|---|
| Dimensiones (L × A × H) | _por definir_ |
| Peso | _por definir_ |
| Tipo de tracción | Diferencial, 2 motores BLDC de hoverboard 6,5" (control FOC) |
| Velocidad máxima | _por definir_ |
| Batería | 2× Li-ion 10S2P 36 V · 4,4 Ah · 158 Wh (316 Wh en total) |
| Autonomía estimada | ~1,4 h, estimación preliminar (ver [presupuesto de potencia](electrica/presupuesto_potencia.csv)) |
| Computador principal | NVIDIA Jetson Orin Nano Dev Kit + Arduino Mega 2560 |
| Sensores | RPLIDAR C1, Orbbec Gemini Plus, IMU HFI-B9, IMU MPU-9250, Hiwonder WonderMV |

## Estado actual

| Área | Estado |
|---|---|
| Diseño 3D | 🔲 Pendiente |
| Plano eléctrico | 🟡 Rev. 1.0 en revisión ([pendientes](electrica/revision_plano.md)) |
| URDF | 🟡 Plantilla inicial (medidas provisorias) |
| BOM | 🔲 Pendiente |
| Fabricación | 🔲 Pendiente |

🔲 Pendiente · 🟡 En progreso · ✅ Listo

## Estructura del repositorio

```
.
├── mecanica/
│   ├── cad/          # Archivos fuente del CAD (formato nativo)
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

```bash
# Dentro de un workspace de ROS 2
cd ~/ros2_ws/src
git clone https://github.com/AndesRobot-Oficial/Structure-Embedded-Systems_MILO.git
cd ~/ros2_ws
colcon build --packages-select milo_description
source install/setup.bash
ros2 launch milo_description display.launch.py
```

## Archivos pesados (Git LFS)

Los archivos CAD, STEP, STL y binarios se guardan con [Git LFS](https://git-lfs.com). Antes de clonar o subir archivos:

```bash
git lfs install
```

Las extensiones que van a LFS están en [`.gitattributes`](.gitattributes).

## Cómo contribuir

1. Crea una rama: `git checkout -b feature/descripcion-corta`
2. Sube archivos fuente **y** sus exportaciones (ej. el CAD nativo y su STEP).
3. Si cambias algo que afecta al brazo, actualiza [`interfaz_brazo/`](interfaz_brazo/README.md) y avísale a ese equipo.
4. Registra los cambios importantes en [`CHANGELOG.md`](CHANGELOG.md) y las decisiones en [`docs/decisiones.md`](docs/decisiones.md).
5. Abre un Pull Request.

## Equipo

| Nombre | Rol |
|---|---|
| _por completar_ | |

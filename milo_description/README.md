# milo_description

URDF del robot con masas calculadas: paquete ROS 2 (`andesrobot_description`) con el modelo URDF/xacro de MILO, exportado del CAD de Fusion 360.

- Modelo principal: [`urdf/andesrobot.urdf.xacro`](urdf/andesrobot.urdf.xacro)
- Mallas del CAD: [`meshes/`](meshes/)
- Frames, medidas y argumentos del xacro: [`docs/ROBOT.md`](docs/ROBOT.md)
- Masas: estimadas (rev. 0), no salen del CAD; ver [`docs/ROBOT.md`](docs/ROBOT.md)

El modelo incluye la base diferencial, la columna con el elevador, el RPLIDAR C1, la IMU y los links del brazo y la pinza.

## Visualizar

```bash
cd ~/ros2_ws/src
git clone https://github.com/AndesRobot-Oficial/Structure-Embedded-Systems_MILO.git
cd ~/ros2_ws
colcon build --packages-select andesrobot_description
source install/setup.bash
ros2 launch andesrobot_description display.launch.py
```

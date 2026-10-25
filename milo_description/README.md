# milo_description

Paquete ROS 2 con el modelo URDF/xacro de la base de MILO.

> ⚠ Las medidas, masas y posiciones de sensores en `urdf/milo.urdf.xacro` son **provisorias**. Reemplazarlas por las del CAD.

## Frames

| Frame | Descripción |
|---|---|
| `base_footprint` | Proyección de la base en el suelo |
| `base_link` | Centro del eje de las ruedas motrices |
| `left_wheel_link` / `right_wheel_link` | Ruedas motrices |
| `caster_link` | Rueda loca |
| `laser_link` | LiDAR |
| `camera_link` | Cámara |
| `imu_link` | IMU |
| `arm_mount_link` | Punto de montaje del brazo (ver `interfaz_brazo/`) |

## Cómo pasar del CAD al URDF
1. Exporta cada pieza móvil como malla (STL o DAE) **en metros** o ajusta `scale`, y guárdala en `meshes/`.
2. Copia masa, centro de masa e inercia de las propiedades físicas del CAD a cada `<inertial>`.
3. Mide la posición real de cada sensor respecto a `base_link` y actualiza los `<origin>`.
4. Verifica con `ros2 launch milo_description display.launch.py` y `check_urdf`.

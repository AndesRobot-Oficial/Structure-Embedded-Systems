# AndesRobot — modelo

Convención REP-103/105: +X adelante, +Y izquierda, +Z arriba.

## Frames
| Frame | Dónde |
|---|---|
| `base_footprint` | suelo, bajo el centro del eje de las ruedas motrices |
| `base_link` | centro del eje de ruedas (centro de rotación), z = 0.08255 m |
| `laser` | RPLIDAR C1, x = 0.408, z = 0.363 (desde base_footprint), 0° hacia +X |
| `imu_link_1` | x = 0.13, z = 0.103 |

## Base diferencial
- Ruedas: radio 0.08255 m, ancho 0.045 m, **separación 0.3604 m** (centro a centro de la banda).
- Rueda loca delantera en x = 0.35 m. Altura montaje→suelo 0.103 m.
  `caster_wheel_radius` = 0.025 m es **provisorio: medir la rueda real**.

## Masa y estabilidad
- Masas **estimadas** (rev. 0), detalle en `docs/calculos/masas.md` del repo. Total ~31,6 kg.
  Las masas del CAD no se usan: Fusion las exportó con material por defecto (1,06 g/cm³; acero en la muñeca).
- `batteries_link` (2,2 kg) en lo más bajo del chasis y `drivers_link` (1,3 kg, 7× TB6600) sobre la base hacia atrás.
  Reemplazan al lastre ficticio de 12 kg.
- Brazo recogido: centro de masa ~0,09 m delante del eje y a ~0,48 m de altura. Vuelca hacia atrás
  sobre el eje con ~1,8 m/s² de aceleración (1,4 m/s² con el elevador arriba).
- Diff drive: aceleración 0.8 m/s² y torque máx. 5 N·m por rueda. Con más torque que el momento del peso
  sobre el eje el robot levanta la rueda loca y se vuelca al arrancar o al chocar.

## RPLIDAR C1 (simulado)
360°, 500 muestras/vuelta (0.72°), 10 Hz, 0.05–12 m, ruido σ = 12 mm.
La columna tapa ±4.5° detrás del sensor (0.38–0.44 m): se filtra en `andesrobot_slam/config/rplidar_c1_filter.yaml`.
El plano de escaneo (+30 mm sobre la base del sensor) es estimado: confirmar con el plano mecánico del C1.

## Argumentos del xacro
| Arg | Default | Uso |
|---|---|---|
| `lock_arm` | false | true = brazo, lift y dedos fijos (simulación de base) |
| `simple_collision` | false | true = colisiones con cajas/cilindros en vez de mallas CAD |
| `sim_lidar` / `sim_imu` | true | apagar sensores simulados (depuración) |
| `use_hardware` | false | true = ros2_control del hoverboard (Milo físico) |
| `hoverboard_port` | /dev/hoverboard | puerto serie del hoverboard |

## Pendiente antes del robot real
- Las articulaciones del brazo son `continuous` sin límites: reemplazar por `revolute` con límites medidos.
- Verificar el yaw de `laser_joint` según cómo quede montado el conector del C1.
- Calibrar `wheel_radius` y `wheel_separation` en `milo_controllers.yaml` (ver README, "Primera prueba").
- Reemplazar las masas estimadas por pesos reales (ruedas, baterías, piezas del brazo).

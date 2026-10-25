# Interfaz Base ↔ Brazo

Acuerdo entre el equipo de base y el equipo del brazo. **Cualquier cambio aquí debe conversarse con ambos equipos antes de hacer merge.**

| Versión | Fecha | Cambio | Aprobado por (base / brazo) |
|---|---|---|---|
| 0.1 | _por completar_ | Borrador inicial | / |

## 1. Montaje mecánico

| Ítem | Valor |
|---|---|
| Ubicación del montaje respecto a `base_link` (x, y, z) | _por definir_ |
| Patrón de pernos (cantidad, métrica, distancia entre centros) | _por definir_ |
| Espesor / material de la placa de montaje | _por definir_ |
| Volumen libre disponible para el brazo | _por definir_ |
| Masa máxima del brazo que soporta la base | _por definir_ |
| Momento máximo admisible en el montaje | _por definir_ |

Plano o STEP de la placa de montaje: _link por agregar_.

## 2. Frame en el URDF

La base publica el frame **`arm_mount_link`** (unido a `base_link` por un joint fijo `arm_mount_joint`).
El equipo del brazo conecta el primer link de su URDF a `arm_mount_link`.
Convención de ejes: X hacia adelante del robot, Z hacia arriba (REP 103).

## 3. Alimentación

| Ítem | Valor |
|---|---|
| Voltaje entregado | _por definir_ |
| Corriente continua máxima | _por definir_ |
| Corriente pico máxima | _por definir_ |
| Conector | _por definir_ |
| Protección (fusible) | _por definir_ |
| ¿La parada de emergencia corta la potencia del brazo? | Sí (obligatorio) |

## 4. Comunicación

| Ítem | Valor |
|---|---|
| Medio (USB / Ethernet / CAN / otro) | _por definir_ |
| Conector y ubicación | _por definir_ |
| Paso de cables (ruta y diámetro disponible) | _por definir_ |

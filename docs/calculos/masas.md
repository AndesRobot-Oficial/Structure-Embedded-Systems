# Estimación de masas — rev. 0

Primera estimación sin pesar piezas. Reemplazar cada valor por el peso real cuando se mida.

**Total estimado: ~31 kg** (sin la cabeza ni las cámaras, que aún no están en el modelo).

> Las masas del URDF actual no sirven: Fusion exportó casi todas las piezas con un material por defecto de 1,06 g/cm³, y la muñeca y los dedos con acero (7,85 g/cm³).

## Resumen

| Grupo | Masa |
|---|--:|
| Estructura (chasis 3030 + columna 6060) | 9,4 kg |
| Ruedas y rueda loca | 6,1 kg |
| Electrónica y cableado | 7,2 kg |
| Elevador (motor + carro) | 1,1 kg |
| Brazo con motores y pinza | 6,1 kg |
| Placas, escuadras y tornillería | 1,5 kg |
| **Total** | **~31,4 kg** |

## Estructura

| Parte | Cálculo | Masa |
|---|---|--:|
| Chasis, V-slot 3030 | ~5,5 m de perfil (medido en el CAD) × ~1,0 kg/m | 5,5 kg |
| Columna, V-slot 6060 | 1,5 m × ~2,6 kg/m | 3,9 kg |

## Tracción

| Parte | Cálculo | Masa |
|---|---|--:|
| Rueda motor hoverboard 6,5" 36 V 350 W | ~3,0 kg c/u, 2 ruedas | 6,0 kg |
| Rueda loca | Estimado | 0,1 kg |

## Electrónica

| Parte | Masa |
|---|--:|
| 2× batería 10S2P (20 celdas 18650 c/u + BMS) | 2,2 kg |
| 7× driver TB6600 | 1,3 kg |
| Cables y conectores (137 cables) | 0,8 kg |
| Conversor 42 → 24 V 20 A | 0,6 kg |
| Monitor 11,6" | 0,6 kg |
| Victron GX Touch 50 | 0,25 kg |
| Orbbec Gemini Plus | 0,25 kg |
| Jetson Orin Nano Dev Kit | 0,2 kg |
| Conversores 24 → 12 V y 24 → 6,6 V | 0,25 kg |
| Placa hoverboard, hub USB, seta de emergencia | 0,45 kg |
| RPLIDAR C1, IMUs, WonderMV, Arduino Mega, hub MST | 0,25 kg |
| **Subtotal** | **7,2 kg** |

## Elevador

| Parte | Masa |
|---|--:|
| Motor NEMA 23 1,26 N·m | 0,7 kg |
| Carro (PLA + ruedas V-slot) | 0,4 kg |

## Brazo

PLA al 40 % de relleno: densidad efectiva ≈ 0,75 g/cm³ (paredes y tapas sólidas + 40 % de relleno), aplicada al volumen de cada pieza en el CAD.
PVC sanitario con pared de ~1,8 mm: Ø75 mm ≈ 0,58 kg/m y Ø50 mm ≈ 0,38 kg/m.

| Eslabón | PLA | Tubo PVC | Motor que lleva | Masa |
|---|--:|--:|---|--:|
| Base del brazo (`arm_base_link_1`) | 0,27 kg | — | NEMA 23 1,26 N·m, base giratoria (0,7 kg) | 0,97 kg |
| Eslabón 1 (`link_1_1`) | 0,31 kg | — | NEMA 23 2,9 N·m, hombro (1,0 kg) | 1,31 kg |
| Brazo (`link_2_1`) | 0,84 kg | Ø75 × 0,35 m (0,20 kg) | NEMA 23 1,26 N·m, codo (0,7 kg) | 1,74 kg |
| Antebrazo (`link_3_1`) | 0,47 kg | Ø50 × 0,32 m (0,12 kg) | NEMA 17, muñeca 1 (0,35 kg) | 0,94 kg |
| Muñeca 1 (`link_4_1`) | 0,16 kg | — | NEMA 17, muñeca 2 (0,35 kg) | 0,51 kg |
| Muñeca 2 (`link_5_1`) | 0,16 kg | — | NEMA 17, muñeca 3 (0,35 kg) | 0,51 kg |
| Muñeca 3 (`link_6_1`) | 0,07 kg | — | Servo LF-20MG, pinza (0,06 kg) | 0,13 kg |
| 2 dedos | 0,03 kg | — | — | 0,03 kg |
| **Total** | | | | **6,1 kg** |

Se supone que cada motor va montado en el eslabón anterior a la articulación que mueve.
La carga útil de 2 kg en la punta va aparte.

## Supuestos por confirmar

- **Perfiles:** el peso por metro varía según el fabricante; confirmar con su ficha técnica.
- **Ruedas:** 3,0 kg por similitud con motores equivalentes; pesar una.
- **Motores:** el NEMA 23 de 2,9 N·m es ~1 kg (dato del equipo). Los de 1,26 N·m (~0,7 kg) y los NEMA 17 (~0,35 kg) son valores típicos para su tamaño.
- **Tubos de PVC:** diámetros medidos en el CAD; largos aproximados por la distancia entre articulaciones.
- **Electrónica:** datasheets donde existen, el resto estimado.
- **Falta:** cabeza, soporte de cámaras y la tornillería real (ver [BOM](../../bom/README.md)).

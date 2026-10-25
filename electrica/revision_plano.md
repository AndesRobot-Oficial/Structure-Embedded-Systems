# Revisión del plano eléctrico — rev. 1.0

Revisión de [`esquematicos/milo_plano_electrico.json`](esquematicos/milo_plano_electrico.json). Marcar cada punto cuando se resuelva y subir una nueva revisión del plano.

Severidad: 🔴 seguridad / puede dañar algo · 🟠 puede fallar en funcionamiento · 🟡 mejora o dato faltante

## 🔴 Seguridad

- [ ] **1. La parada de emergencia es solo por software.** Los contactos NC van a una entrada del Jetson (pin 7) y del Mega (D18); ninguno corta potencia. La placa del hoverboard ni siquiera la ve: si el Jetson se cuelga, las ruedas siguen con el último comando. El reglamento exige que *el robot y todas sus partes dejen de moverse inmediatamente* y se revisa en la inspección. **Propuesta:** que la seta corte por hardware la potencia de actuadores (bus 36 V de la placa hoverboard y salida 24 V a los TB6600) mediante un contactor o relé de potencia dimensionado para la corriente, y mantener el segundo contacto NC como aviso al software. El Jetson y los sensores pueden seguir encendidos.
- [ ] **2. No hay fusibles ni interruptor general.** Ningún componente tiene protección entre la batería y la carga; un cortocircuito en el bus de 36 V solo lo limitaría el BMS. **Propuesta:** fusible por batería, interruptor general de llave, fusible en la entrada de la placa hoverboard, en la entrada del conversor 42→24 V y uno por rama de 24 V (TB6600) y de 12 V (Jetson, hub).
- [ ] **3. Cuatro cables de batería están en 24 AWG.** `w1792893666820`, `w1792893677780`, `w1792893724422` y `w1792893736372` (Batería 1 y 2 al conversor 42→24 V y a la placa hoverboard) quedaron como "Señal" en 24 AWG. Por ahí pasa la corriente de las ruedas (hasta ~17 A). Deben ser del mismo calibre que el resto del bus (12 AWG) o eliminarse si son duplicados.
- [ ] **4. Baterías en paralelo directo.** Ambos packs quedan unidos en el bus de 36 V sin diodo ni interruptor por pack. Si se conectan con voltajes distintos, circula una corriente grande entre ellos. Definir si van en paralelo (y conectarlas solo con el mismo voltaje, con un interruptor por pack) o si cada una alimenta un subsistema distinto.

## 🟠 Funcionamiento

- [ ] **5. Conversor 42→24 V con entrada mínima de 30 V.** Un pack 10S baja de 30 V (3,0 V/celda) antes de que corte el BMS, así que el conversor se apagará antes que la placa hoverboard. Confirmar el voltaje de corte del BMS y avisar por software antes de llegar ahí.
- [ ] **6. Hub DisplayPort MST.** NVIDIA indica que el Orin Nano no permite dividir una salida en dos pantallas independientes; lo soportado es la misma imagen en ambas. El monitor de 11.6" y la GX Touch 50 mostrarían lo mismo y con resoluciones distintas. Considerar una sola pantalla o una segunda pantalla por USB.
- [ ] **7. Victron GX Touch 50.** Está hecha para los equipos GX de Victron: el táctil usa el canal DDC del HDMI, y hay reportes de problemas al usarla con otros computadores. Probarla con el Jetson antes de integrarla o reemplazarla por una pantalla HDMI genérica.
- [ ] **8. UART del hoverboard a 3,3 V.** Poner el puente del CH340G en 3,3 V: algunos puertos UART de estas placas no toleran 5 V.
- [ ] **9. Pull-up de la entrada E-STOP del Jetson.** La seta lleva el pin 7 a GND; sin pull-up la entrada queda flotando al presionarla. Agregar una resistencia a 3V3 (pin 1) o configurar el pull-up. En el Mega usar `INPUT_PULLUP`.
- [ ] **10. ENA de los TB6600.** En el TB6600 el optoacoplador ENA activo **deshabilita** el driver. Con cátodo común, `EN = HIGH` apaga el motor; dejarlo así en el firmware y documentarlo.
- [ ] **11. Monitor alimentado desde el hub USB.** Un puerto USB 3.0 entrega 0,9 A (4,5 W) si el hub no da más; un monitor de 11.6" puede necesitar más. Revisar la corriente por puerto del hub y el consumo del monitor.

## 🟡 Datos faltantes y mejoras

- [ ] **12. Pin VIN del Mega etiquetado 7,4 V pero sin conexión.** Hoy el Mega se alimenta por el USB del Jetson. Si se quiere alimentar aparte, 6,6 V queda bajo el mínimo de 7 V de VIN. Quitar la etiqueta o definir la fuente.
- [ ] **13. Puerto 7 del hub USB marcado como entrada.** Debería ser salida como los otros.
- [ ] **14. Corriente de NEMA 17 sin confirmar** ("~1,5 A/fase, confirmar en la etiqueta"). Se necesita para ajustar los DIP del TB6600 y para el presupuesto de potencia.
- [ ] **15. Falta el conector de carga** de las baterías y el procedimiento de carga.
- [ ] **16. Falta un medidor o aviso de batería baja** (voltaje del bus hacia el Jetson o el Mega).
- [ ] **17. Viaje en avión.** Cada pack es de 158 Wh, justo bajo el límite de 160 Wh; entre 100 y 160 Wh las aerolíneas suelen pedir aprobación previa. Revisar con la aerolínea antes de RoboCup 2027.

## Presupuesto de potencia

Ver [`presupuesto_potencia.csv`](presupuesto_potencia.csv). Con los valores que hay (faltan varios periféricos), el consumo típico es de unos **160 W** en las cargas, unos **180 W** desde la batería con conversores al 90 %. Con 316 Wh y usando el 80 %, eso da **~1,4 h** de autonomía. Los 7 motores paso a paso aportan ~90 W aunque estén quietos, porque mantienen la corriente; sin ellos la autonomía estimada sube a ~3,3 h. Si el driver reduce la corriente en reposo, la cifra mejora.

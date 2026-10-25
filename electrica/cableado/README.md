# Cableado

[`tabla_cableado.csv`](tabla_cableado.csv): los 137 cables del plano, con su ID de etiqueta (C001…), extremos, señal, color y calibre. La columna `notas` guarda el ID del cable en el plano.

No se edita a mano salvo `largo_mm`: se regenera desde el plano con

```bash
python electrica/herramientas/exportar_cableado.py electrica/esquematicos/milo_plano_electrico.json electrica/cableado/tabla_cableado.csv
```

Los IDs y los largos ya medidos se conservan al regenerar. Cada cable lleva una etiqueta física con su ID.

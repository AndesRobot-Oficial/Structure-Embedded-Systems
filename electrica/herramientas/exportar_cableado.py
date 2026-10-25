"""Genera la tabla de cableado (CSV) a partir del plano de Mesa de Cableado (JSON).

Uso:
    python electrica/herramientas/exportar_cableado.py \
        electrica/esquematicos/milo_plano_electrico.json \
        electrica/cableado/tabla_cableado.csv

Volver a correrlo cada vez que se modifique el plano. Si el CSV de salida ya
existe, se conservan el ID de cada cable (su etiqueta física) y la columna
largo_mm, que se llena a mano al medir en el robot.
"""
import csv
import json
import sys
from pathlib import Path

COLORES = {
    "#d6302f": "Rojo", "#ef4444": "Rojo",
    "#1d1f1f": "Negro", "#111827": "Negro",
    "#2f9a4f": "Verde", "#2c6fd1": "Azul",
    "#e5b80b": "Amarillo", "#e8731a": "Naranjo",
    "#f59e0b": "Amarillo", "#8a918e": "Gris",
}

CAMPOS = ["id", "desde", "pin_desde", "hacia", "pin_hacia", "senal",
          "color", "calibre", "largo_mm", "notas"]


def main(entrada: str, salida: str) -> None:
    plano = json.loads(Path(entrada).read_text(encoding="utf-8"))
    nodos = {n["id"]: n for n in plano["nodes"]}

    # Conserva el ID de etiqueta (C001...) y el largo de cada cable ya existente,
    # para que las etiquetas físicas no cambien al editar el plano.
    previos = {}
    if Path(salida).exists():
        with open(salida, encoding="utf-8") as f:
            previos = {r["notas"]: r for r in csv.DictReader(f)}
    usados = {int(r["id"][1:]) for r in previos.values() if r["id"][1:].isdigit()}
    siguiente = max(usados, default=0) + 1

    filas = []
    for w in plano["wires"]:
        a, b = nodos[w["from"]["node"]], nodos[w["to"]["node"]]
        previo = previos.get(w["id"], {})
        cid = previo.get("id")
        if not cid:
            cid = f"C{siguiente:03d}"
            siguiente += 1
        largos = {cid: previo.get("largo_mm", "")}
        filas.append({
            "id": cid,
            "desde": a["name"], "pin_desde": a["pins"][w["from"]["pin"]],
            "hacia": b["name"], "pin_hacia": b["pins"][w["to"]["pin"]],
            "senal": w.get("label", ""),
            "color": COLORES.get(w.get("color", "").lower(), w.get("color", "")),
            "calibre": w.get("gauge", ""),
            "largo_mm": largos.get(cid, ""),
            "notas": w["id"],
        })

    with open(salida, "w", newline="", encoding="utf-8") as f:
        wr = csv.DictWriter(f, fieldnames=CAMPOS, lineterminator="\n")
        wr.writeheader()
        wr.writerows(filas)
    print(f"{len(filas)} cables escritos en {salida}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])

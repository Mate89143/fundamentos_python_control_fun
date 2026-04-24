transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0

for t in transacciones:
    if t["estado"] != "completada":
        continue

    if t["monto"] <= 0:
        continue

    total_procesado += t["monto"]
    print(f"Procesada: {t['id']}")

print(f"Total: {total_procesado}")

# Procesa solo transacciones válidas ignorando las que no cumplen condiciones.
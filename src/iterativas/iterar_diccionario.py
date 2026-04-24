usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

for valor in usuario.values():
    print(valor)

# Recorre un diccionario mostrando claves, valores y pares clave-valor usando diferentes métodos.
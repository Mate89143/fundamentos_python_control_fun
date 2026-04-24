encontrado = False

for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i*j}")
            encontrado = True
            break

    if encontrado:
        break

# Usa una variable bandera para salir de múltiples bucles cuando se cumple una condición.
for i in range(1, 4):
    print(f"Grupo {i}:")

    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue

        print(f"  Elemento {j}")

    print("Fin del grupo\n")

# Controla un bucle anidado usando continue para saltar una iteración específica.
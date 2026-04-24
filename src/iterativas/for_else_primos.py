numeros = [4, 6, 8, 9, 10, 12]

for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"Primo encontrado: {num}")
        break
else:
    print("No se encontró ningún número primo")

# Usa else en un for para ejecutar código solo si el bucle no se interrumpe con break.
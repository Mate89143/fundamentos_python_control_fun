numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0

for num in numeros:
    if num % 3 == 0:
        print(f"Omitiendo {num}")
        continue

    suma += num
    print(f"Añadiendo {num}: suma = {suma}")

    if suma > limite:
        print("Límite superado")
        break

# Combina continue para omitir valores y break para detener el bucle cuando se supera un límite.
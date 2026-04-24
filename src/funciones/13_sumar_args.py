def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar(1, 2))
print(sumar(1, 2, 3, 4, 5))
print(sumar())

# Este ejercicio utiliza *args para sumar una cantidad variable de números.
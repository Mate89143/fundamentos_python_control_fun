def calcular_factorial(n):
    resultado = 1

    while n > 0:
        resultado *= n
        n -= 1

    return resultado

print(calcular_factorial(5))

# Calcula el factorial de un número multiplicando todos los valores desde n hasta 1.
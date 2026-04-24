def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []

for num in range(2, 20):
    if es_primo(num):
        primos.append(num)

print(primos)

# Detecta y almacena números primos dentro de un rango usando una función de validación.
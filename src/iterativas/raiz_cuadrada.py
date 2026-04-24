def raiz(numero):
    aprox = numero / 2

    while abs(aprox**2 - numero) > 0.001:
        aprox = (aprox + numero/aprox) / 2

    return aprox

print(raiz(25))

# Aproxima la raíz cuadrada de un número usando iteraciones sucesivas hasta lograr precisión.
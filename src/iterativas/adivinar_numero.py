import random

objetivo = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    intentos += 1
    numero = int(input("Adivina (1-10): "))

    if numero == objetivo:
        adivinado = True
        print("¡Correcto!")
    else:
        print("Incorrecto")

# Juego de adivinar un número con intentos limitados y retroalimentación al usuario.
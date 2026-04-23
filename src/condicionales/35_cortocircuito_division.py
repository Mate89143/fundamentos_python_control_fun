dividendo = 10
divisor = 0

if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")

# Usa cortocircuito para evitar dividir entre cero, evaluando primero si el divisor es diferente de 0.
def validar():
    while True:
        valor = int(input("Número (0-10): "))

        if 0 <= valor <= 10:
            return valor
        
# Valida que un número ingresado esté dentro de un rango específico antes de aceptarlo.
def dividir_seguro(a, b):
    if b == 0:
        print("Error: División por cero")
        return None

    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))

# Este ejercicio realiza una división segura evitando dividir por cero.
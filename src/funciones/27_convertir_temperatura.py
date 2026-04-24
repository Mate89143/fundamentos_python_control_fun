def convertir_temperatura(valor, origen, destino):
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    if origen == destino:
        return valor

    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:
        celsius = valor

    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:
        return celsius

print(convertir_temperatura(25, 'C', 'F'))
print(convertir_temperatura(98.6, 'F', 'C'))
print(convertir_temperatura(0, 'C', 'K'))
print(convertir_temperatura(20, 'X', 'Y'))

# Este ejercicio convierte temperaturas entre Celsius, Fahrenheit y Kelvin.
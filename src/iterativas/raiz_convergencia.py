def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero/aproximacion) / 2
        iteracion += 1
    else:
        print("Convergencia alcanzada")
        return aproximacion

    print("No convergió")
    return aproximacion

# Calcula una raíz aproximada y usa else en while para indicar si se alcanzó convergencia.
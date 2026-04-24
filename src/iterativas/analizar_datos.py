def analizar_datos(valores, umbral):
    tiene_advertencias = False

    for valor in valores:
        if valor > umbral:
            tiene_advertencias = True
            print("Advertencia")
        else:
            pass
    else:
        if not tiene_advertencias:
            print("Todo normal")
            return "OK"

    return "ADVERTENCIA"

# Analiza valores comparándolos con un umbral y usa pass y else para controlar el flujo.
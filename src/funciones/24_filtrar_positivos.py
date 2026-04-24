def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []

    return [num for num in numeros if num > 0]

# Este ejercicio filtra números positivos asegurando que el input sea una lista.
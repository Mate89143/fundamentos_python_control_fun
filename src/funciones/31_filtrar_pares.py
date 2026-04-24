def filtrar_pares(lista):
    """
    Filtra los números pares de una lista.

    Parameters
    ----------
    lista : list
        Lista de números enteros

    Returns
    -------
    list
        Nueva lista que contiene solo los números pares
    """
    return [num for num in lista if num % 2 == 0]

# Acceder al docstring directamente
print(filtrar_pares.__doc__)

# Este ejercicio filtra números pares usando docstring estilo NumPy.
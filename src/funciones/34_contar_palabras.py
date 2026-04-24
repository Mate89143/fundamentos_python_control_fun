def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.

    Args:
        texto (str): El texto a analizar

    Returns:
        int: El número de palabras encontradas
    """
    return len(texto.split())

# Acceder al docstring directamente
print(contar_palabras.__doc__)

# Este ejercicio cuenta cuántas palabras hay en un texto.
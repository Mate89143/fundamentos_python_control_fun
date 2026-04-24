def formatear_nombre(nombre, apellido):
    """
    Formatea un nombre completo en formato "Apellido, Nombre".

    Args:
        nombre: Nombre de la persona
        apellido: Apellido de la persona

    Returns:
        Cadena formateada como "Apellido, Nombre"

    Ejemplo:
        >>> formatear_nombre("Juan", "Pérez")
        'Pérez, Juan'
    """
    return f"{apellido}, {nombre}"

# Acceder al docstring directamente
print(formatear_nombre.__doc__)

# Este ejercicio formatea un nombre completo con docstring y ejemplo.
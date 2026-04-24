def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)

# Este ejercicio crea un diccionario usando múltiples parámetros y argumentos por nombre.
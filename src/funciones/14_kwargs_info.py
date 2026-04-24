def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)

# Este ejercicio usa **kwargs para manejar múltiples argumentos con nombre.
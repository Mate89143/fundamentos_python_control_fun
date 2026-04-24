while True:
    entrada = input("Escribe algo (o 'salir' para terminar): ")

    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break

    print(f"Has escrito: {entrada}")

# Permite al usuario ingresar datos hasta que escriba "salir", momento en el que el programa finaliza.
def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print("Usuario encontrado")
            return usuario
    else:
        print("Usuario no encontrado, creando uno nuevo")
        nuevo = {"nombre": nombre}
        usuarios.append(nuevo)
        return nuevo
    
# Busca un usuario en una lista y si no existe lo crea usando la cláusula else.
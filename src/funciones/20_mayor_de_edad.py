def es_mayor_de_edad(edad):
    return edad >= 18

def es_correo_valido(email):
    return "@" in email and "." in email

usuario_edad = 16
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado")

# Este ejercicio usa funciones booleanas para validar condiciones.
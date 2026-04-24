def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
            continue

        if caracter.islower():
            tiene_minuscula = True
            continue

        if caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero

contraseñas = ["abc123", "Password", "Password1"]

for pwd in contraseñas:
    print(validar_contraseña(pwd))

# Verifica si una contraseña cumple requisitos básicos como longitud, mayúsculas, minúsculas y números.
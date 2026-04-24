def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]
    errores = []

    for campo in campos_requeridos:
        if campo not in datos:
            errores.append("Falta campo")
            break
        elif not datos[campo]:
            errores.append("Campo vacío")
            break
    else:
        if "@" not in datos["email"]:
            errores.append("Email inválido")

    if errores:
        return {"valido": False}
    else:
        return {"valido": True}
    
# Valida un formulario verificando campos obligatorios y usando else para continuar validaciones si todo está correcto.
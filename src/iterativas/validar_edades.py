def validar_edades(lista_edades):
    for edad in lista_edades:
        if edad < 0:
            print("Edad inválida")
            break
    else:
        print("Todas las edades son válidas")
        return True

    return False

# Verifica que todas las edades sean válidas usando else para confirmar que no hubo errores.
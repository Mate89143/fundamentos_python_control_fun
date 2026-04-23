edad = 20

match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")
    
# Clasifica la edad usando match-case con condiciones (guardas), determinando si es menor, adulto o adulto mayor.
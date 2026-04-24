def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)
print(f"Precio final: {total}")

# Este ejercicio calcula el precio final aplicando un impuesto mediante parámetros.
def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(f"Suma: {suma}")
print(f"Promedio: {media}")
print(f"Mínimo: {menor}")
print(f"Máximo: {mayor}")

# Este ejercicio devuelve múltiples valores (tupla) con estadísticas de una lista.
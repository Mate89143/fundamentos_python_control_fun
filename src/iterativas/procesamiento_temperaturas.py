temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

max_temp = max(temperaturas)
indice = temperaturas.index(max_temp)

print(f"Día más caluroso: {dias[indice]} con {max_temp}")

promedio = sum(temperaturas) / len(temperaturas)
print(f"Promedio: {promedio}")

for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]} encima del promedio")

# Procesa temperaturas para encontrar el máximo, el promedio y los días que superan el promedio.
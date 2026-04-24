def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"

pago1 = calcular_pago(40)
pago2 = calcular_pago(35, 20)
pago3 = calcular_pago(30, moneda="USD")
pago4 = calcular_pago(horas=25, tarifa=18, moneda="GBP")

print(pago1)
print(pago2)
print(pago3)
print(pago4)

# Este ejercicio combina distintos tipos de parámetros para calcular pagos.
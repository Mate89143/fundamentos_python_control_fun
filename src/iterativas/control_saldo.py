saldo = 1000

while saldo > 0:
    gasto = float(input("Gasto (0 para salir): "))

    if gasto == 0:
        break

    if gasto > saldo:
        continue

    saldo -= gasto
    print("Saldo:", saldo)

# Simula un control de saldo bancario donde el usuario puede gastar dinero hasta agotarlo o salir.
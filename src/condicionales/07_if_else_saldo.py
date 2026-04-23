saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")

# Verifica si hay suficiente dinero para hacer un retiro. Si alcanza el saldo, lo descuenta; si no, muestra que no hay fondos suficientes.
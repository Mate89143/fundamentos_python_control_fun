acceso_registrado = True

acceso_permitido = False

if acceso_permitido or acceso_registrado:
    print("Acceso concedido.")

# Este ejemplo demuestra la evaluación de cortocircuito, ya que si la primera condición fuera True, Python ni siquiera evaluaría la segunda.
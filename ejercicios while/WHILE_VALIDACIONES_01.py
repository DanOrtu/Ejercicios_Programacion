# 1. Pedir el ingreso de una clave.
# Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados. 


ingreso = int(input("BIENVENIDO.\nPor favor ingrese la clave: "))

while ingreso != 3791:
    ingreso = int(input("ERROR \nIngrese la clave correcta: "))

print("BIENVENIDO, USUARIO.")


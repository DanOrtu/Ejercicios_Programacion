# Pedir el ingreso de una clave. 
# Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos. 

intentos = 0

bandera_accedio = False
clave = int(input("BIENVENIDO\nIngrese su clave: "))

intentos += 1

while bandera_accedio == False and clave != 4682:
    clave = int(input("ERROR.\nIngrese la clave correcta: "))
    intentos += 1
    if intentos >= 3:
        break

if intentos >=3:
    print("ERROR. Usted no es el usuario.\nCerrando sesión.")

if clave == 4682:
    bandera_accedio = True
    print("BIENVENIDO USUARIO")

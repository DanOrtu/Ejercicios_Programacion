# 3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.

def pedir_cadena():
    cadena = str(input("Ingrese una cadena X: "))
    return cadena

#########Main###########

mostrar_cadena = pedir_cadena()

print(mostrar_cadena)


#1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne. 
def pedir_numero():
    numero_entero = int(input("Ingrese un numero: "))
    return numero_entero

###########MAIN############

numero_x = pedir_numero()

print(numero_x)


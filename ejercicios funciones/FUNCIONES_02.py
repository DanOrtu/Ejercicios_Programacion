# 2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne. 


def pedir_numero_flotante():
    flotante = float(input("Ingrese un numero flotante: "))
    return flotante

########Main#########

numero_flotante = pedir_numero_flotante()

print(numero_flotante)


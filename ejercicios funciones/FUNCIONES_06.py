# 6. Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar. 

def encontrar_par_o_impar():
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        numero = int(input("no puede ser 0. \nIngrese otro numero: "))
    numero_a_comprobar = numero % 2

    return numero_a_comprobar

###########################

numero_x = encontrar_par_o_impar()

if numero_x == 0:
    print(f"El numero es par")

else:
    print(f"El numero es impar")

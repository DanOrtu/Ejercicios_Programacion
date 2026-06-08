# 8.Define una función que encuentre el máximo de tres números.
# La función debe aceptar tres argumentos y devolver el número más grande. 

def encontrar_maximo(numero_1, numero_2, numero_3):

    maximo = numero_1

    if numero_2 > maximo:
        maximo = numero_2
    
    if numero_3 > maximo:
        maximo = numero_3
    
    return maximo 

########main##########

num_1 = int(input("ingrese un numero: "))
num_2 = int(input("Ingrese otro numero: "))
num_3 = int(input("Ingrese otro numero: "))

maximo = encontrar_maximo(num_1, num_2, num_3)

print(f"El maximo es: {maximo}")


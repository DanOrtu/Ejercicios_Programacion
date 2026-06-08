# 10. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario. 

def retornar_primo():
    bandera_primo = True
    numero = int(input("Ingrese un numero: "))
    if numero == 1: 
        bandera_primo = False
    for i in range(2, numero, 1):
        if numero % i == 0: 
            bandera_primo = False
    return bandera_primo


#####main#####

bandera_primo = retornar_primo()

if bandera_primo == True:
    print("Es un numero primo.")
else:
    print("No es un numero primo.")

# 7. Crea una función que verifique si un número dado es par o impar. 
# La función retorna True si el número es par, False en caso contrario. 

def verificar_par_o_impar():
    bandera_par = True
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        numero = int(input("No puede ser 0.\n Ingrese otro numero: "))
    numero_a_verificiar = numero % 2
    if numero_a_verificiar == 0:
        bandera_par = True
    elif numero_a_verificiar != 0:
        bandera_par = False
    return bandera_par 

########

bandera = verificar_par_o_impar()

if bandera == True:
    print("Es par")
else:
    print("Es impar")

    
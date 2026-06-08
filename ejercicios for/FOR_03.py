# 3 - Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.

numero = int(input("Ingrese un numero: "))

if numero >= 0: 
    for i in range(0, numero + 1 , 1):
        print(i)

if numero < 0:
    for i in range(0, numero -1, -1):
        print(i)


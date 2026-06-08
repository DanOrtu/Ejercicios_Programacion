#12. Ingresar un número. Determinar si el número es primo o no. 

cantidad_de_divisores = 0

numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1, 1):
    if numero % i == 0:
        cantidad_de_divisores += 1

if cantidad_de_divisores == 2:
    print("Es un numero primo.")
else: 
    print("No es un numero primo.")


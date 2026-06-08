#13.Ingresar un número. 
# Mostrar cada número primo que hay entre el 1 y el número ingresado. 
# Informar cuántos números primos se encontraron. 

numero = int(input("Ingrese un numero: "))
contador_primos = 0
for i in range(1, numero + 1, 1):
    contador_divisores = 0
    for j in range(1, i + 1, 1):
        if i % j == 0:
            contador_divisores += 1
    if contador_divisores == 2:
        contador_primos += 1
        print(i)

print(F"Hay {contador_primos} numeros primos. ")

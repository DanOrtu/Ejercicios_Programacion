# 6- Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.
# Mostrar la suma y el promedio de todos los números.


suma = 0

contador = 0

for i in range(10):
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        break
    suma += numero 
    contador += 1

if contador == 0: 
    print("No se puede sacar el promedio. No ingresó numeros")
else:
    promedio = suma / contador
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")


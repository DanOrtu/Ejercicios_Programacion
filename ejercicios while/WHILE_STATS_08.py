# 8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.

i = 0
numero = float(input("Ingrese un numero: "))
minimo = numero
maximo = numero
i += 1
while i < 10: 
    numero = float(input("Ingrese un numero: "))
    if numero < minimo:
        minimo = numero
    if numero > maximo:
        maximo = numero
    i += 1
print(f"Maximo:{maximo}")
print(f"Minimo:{minimo}")
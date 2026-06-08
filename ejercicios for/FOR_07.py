# 7- Ingresar 10 números. Mostrar todos los números excepto el numero 5.

for i in range(10):
    numero = int(input("Ingrese un numero: "))
    if numero == 5: 
        continue
    
    print(f"Su numero es: {numero}")


# 6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
#    Calcular la suma de los números ingresados y el promedio de estos. 


seguir = "si"

suma = 0

contador_de_ingresos = 0

while seguir == "si":
    numero = float(input("Ingrese un numero: "))
    suma += numero
    contador_de_ingresos += 1
    seguir = input("¿Quiere seguir?(si/no): ")

promedio = suma/contador_de_ingresos

print(f"La suma es:{suma}")
print(f"El promedio de estos es:{promedio}")

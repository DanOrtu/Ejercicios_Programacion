# 7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
#    Calcular la suma de los números positivos y el producto de los negativos. 

seguir = "si"

suma_positivos = 0 

producto_negativos = 1

ingreso_negativos = False

while seguir == "si":
    
    numero = float(input("Ingrese un numero: "))
    if numero >= 0:
        suma_positivos += numero
    else:
        producto_negativos *= numero
        ingreso_negativos = True 
    seguir = input("¿Quiere seguir?(si/no): ")

print(f"La suma de los positivos es:{suma_positivos}")

if ingreso_negativos == True:
    print(f"El producto de los negativos es: {producto_negativos}")
else:
    print(f"No se ingresaron numeros negativos.")



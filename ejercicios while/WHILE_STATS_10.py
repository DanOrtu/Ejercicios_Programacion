# 10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. 
#  Calcular la suma de los números ingresados y el promedio de estos. 

suma = 0

contador_ingresos = 0

bandera_seguir_parar = True

while bandera_seguir_parar == True:
    numero = float(input("Ingrese un numero: "))
    suma += numero
    contador_ingresos += 1
    if contador_ingresos >= 5 and contador_ingresos <= 9:
        seguir = input("¿Quiere continuar?(si/no)")
        if seguir != "si":
            bandera_seguir_parar = False
        
    if contador_ingresos == 10:
        bandera_seguir_parar = False 
    
promedio = suma / contador_ingresos

print(f"La suma de los numeros ingresados es de: {suma}")

print(f"El promedio de los numeros es de: {promedio}")


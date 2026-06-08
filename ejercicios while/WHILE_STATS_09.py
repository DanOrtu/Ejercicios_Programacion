# 9.Solicitar al usuario que ingrese como mínimo 5 números. 
#   Calcular la suma de los números ingresados y el promedio de estos. 
suma = 0

contador_ingresos = 0

quiero_seguir = True

while quiero_seguir == True:
    numero = float(input("Ingrese un numero: "))
    suma += numero
    contador_ingresos += 1
    
    if contador_ingresos >= 5:
        pregunta = input("¿Seguir poniendo numeros?: ")
        
        if pregunta != "si":
            quiero_seguir = False

promedio = suma / contador_ingresos


print(f"Suma total: {suma}")

print(f"Promedio: {promedio}")



















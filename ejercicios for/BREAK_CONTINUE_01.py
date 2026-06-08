# 1. Ingresar 10 notas. Si la nota es negativa, ignorarla. 
# Si es mayor que 10 cortar el ingreso. Calcular el promedio con los números válidos. 

suma_de_notas = 0
cantidad_de_notas = 0
for i in range(0, 10, 1):
    notas = float(input("Ingrese una nota: "))
    if notas < 0:
        continue
    if notas >= 0 and notas <= 10: 
        suma_de_notas += notas
        cantidad_de_notas += 1
        print(suma_de_notas)
    if notas > 10:
        break

if cantidad_de_notas == 0:
    print("No se ingresaron notas válidas.")
else:
    promedio = suma_de_notas / cantidad_de_notas 
    print(f"El promedio es: {promedio}")


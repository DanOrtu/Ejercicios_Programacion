# 4. Escribir una función que calcule el área de un rectángulo. 
# La función recibe la base y la altura y retorna el área.

def calcular_area_rectangulo():
    base_rectangulo = float(input("Ingrese la base del rectangulo(Cm): "))
    altura_rectangulo = float(input("Ingrese la altura del rectangulo(Cm): "))
    area = (base_rectangulo * altura_rectangulo) / 2
    return area 

#########Main#######
area_rectagunlo = calcular_area_rectangulo()

print(area_rectagunlo)


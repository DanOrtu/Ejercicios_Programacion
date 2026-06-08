# 5. Escribe una función que calcule el área de un círculo.
# La función debe recibir el radio como parámetro y devolver el área. 

def calcular_area_circulo(radio):
    
    calculo_area_circulo = 3.14 * (radio ** 2)
    
    return calculo_area_circulo

##########Main#######

radio_ingresado = float(input("Ingrese el radio de la circunferencia: "))

area = calcular_area_circulo(radio_ingresado)

print(area)
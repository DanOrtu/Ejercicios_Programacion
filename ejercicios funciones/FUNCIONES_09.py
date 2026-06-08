# 9.Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado. 

def calcular_potencia(base, exponente):
    potencia = base ** exponente
    return potencia

#########main#######

numero_base = int(input("Ingrese un numero base: "))
potenciacion = int(input("Ingrese la potencia: "))

resultado = calcular_potencia(numero_base, potenciacion)
print(f"{numero_base} a la {potenciacion} es: {resultado}")


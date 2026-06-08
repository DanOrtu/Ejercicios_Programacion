# 3. Pedir al usuario el ingreso de una nota.
# La misma debe estar comprendida entre 1 y 10 inclusive. 

nota = float(input("Ingrese la nota del estudiante: "))

while nota < 1 or nota >10:
    nota = float(input("Ingrese nuevamente la nota: "))

print(f"la nota es: {nota}")
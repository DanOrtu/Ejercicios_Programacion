# 4. Solicitarle al usuario el ingreso de un color.
# Validar que el mismo sea Rojo, Verde o Azul. 

color = str(input("Ingrese un color: "))

while color != "Rojo" and color != "rojo" and color != "Verde" and color != "verde" and color != "Azul" and color != "azul":
    color = str(input("Reingrese el color: "))

print(f"Correcto, el color es {color}")

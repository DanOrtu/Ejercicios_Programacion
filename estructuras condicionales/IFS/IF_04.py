# 4. A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no.
#  Para serlo el mismo deberá medir más de 1.80 metros. 

altura = float(input("Ingrese la altura en metros: "))

if altura >= 1.80:
    print("Puede ser pivot.")
else:
    print("No puede ser pivot.")
# 8. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
# el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros: 

# Menos de 160 cm: Base 

# Entre 160 cm y 179 cm: Escolta 

# Entre 180 cm y 199 cm: Alero 

# 200 cm o más: Ala-Pívot o Pívot


altura = float(input("Ingrese la altura en metros: "))

if altura < 1.60:
    print("Base.")
elif altura >= 1.60 and altura <= 1.79:
    print("Escolta")
elif altura >= 1.80 and altura <= 1.99:
    print("Alero")
else:
    print("Ala-Pívot o Pívot.")
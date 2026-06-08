# 9. Los argentinos nativos y por opción desde los dieciséis (16) años y 
# los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar.
#  A partir del ingreso de la edad del usuario y el estado (si es naturalizado o nativo), 
# se deberá informar si es o no posible que la persona concurra a votar en base a la información suministrada. 


edad = int(input("Ingrese su edad: "))
estado = input("Ingrese su estado(naturalizado/nativo): ")

if edad >= 16 and estado == "nativo":
    print("Puede votar.")
elif edad >= 18 and estado == "naturalizado":
    print("Puede votar.")
else:
    print("No puede votar.")
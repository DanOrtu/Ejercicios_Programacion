# 7. Pedirle al usuario su edad, determinar si es mayor (18 años o más), 
# niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).

edad = int(input("Ingrese su edad: "))

if edad < 10:
    print("Es niño.")
elif edad >= 10 and edad <= 13:
    print("Es un pre-adolescente.")
elif edad > 13 and edad <=17:
    print("Es un adolescente.")
else:
    print("Es mayor de edad.")
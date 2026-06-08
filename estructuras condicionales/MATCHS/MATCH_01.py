#1. Realizar un programa que solicite al usuario un número del 1 al 7 
# y muestre el día de la semana correspondiente. Si el número no está entre 1 y 7 mostrar día invalido. 

dia = int(input("Ingrese un numero del 1 al 7: "))

match dia: 
    case 1:
        print("¡Lunes!")
    case 2:
        print("¡Martes!")
    case 3:
        print("¡Miercoles!")
    case 4:
        print("¡Jueves!")
    case 5:
        print("¡Viernes!")
    case 6:
        print("¡Sábado!")
    case 7:
        print("¡Domingo!")
    case _:
        print("Día de la semana inválido.")
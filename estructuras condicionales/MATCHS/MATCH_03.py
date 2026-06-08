#3. Realizar un programa que pida dos números y una operación
# (suma, resta, multiplicación, división -tener en cuenta la división por cero-, resto o potencia). 
# El programa debe realizar la operación correspondiente y mostrar el resultado.
#  Si el resultado es positivo, se mostrará en verde, si es negativo en rojo y si es cero en azul. 

from colorama import Fore, Style, init
init()

numero_a = float(input("Ingrese el primer numero: "))

numero_b = float(input("Ingrese el segundo numero: "))

operacion = input("Ingrese la operación matemática(suma/resta/multiplicaion/division/resto/potencia): ")

match operacion:

    case "suma":

        suma = numero_a + numero_b
        
        if suma > 0:
            print(f"El resultado de la suma es:{Fore.GREEN}{suma}{Style.RESET_ALL}")
        elif suma < 0:
            print(f"El resultado de la suma es:{Fore.RED}{suma}{Style.RESET_ALL}")
        else:
            print(f"El resultado de la suma es:{Fore.BLUE}{suma}{Style.RESET_ALL}")

    case "resta":

        resta = numero_a - numero_b

        if resta > 0:
            print(f"El resultado de la resta es:{Fore.GREEN}{resta}{Style.RESET_ALL}")
        elif resta < 0: 
            print(f"El resultado de la resta es:{Fore.RED}{resta}{Style.RESET_ALL}")
        else:
            print(f"El resultado de la resta es:{Fore.BLUE}{resta}{Style.RESET_ALL}")
    
    case "multiplicacion":

        multi = numero_a * numero_b 

        if multi > 0:
            print(f"El resultado de la multiplicación es:{Fore.GREEN}{multi}{Style.RESET_ALL}")
        elif multi < 0:
            print(f"El resultado de la multiplicación es:{Fore.RED}{multi}{Style.RESET_ALL}")
        else:
            print(f"El resultado de la multiplicación es:{Fore.BLUE}{multi}{Style.RESET_ALL}")
    
    case "division":
        
        if numero_b == 0:
            print("No se puede dividir por 0.")
        else:
            division = numero_a / numero_b
            if division > 0:
                print(f"El resultado de la división es: {Fore.GREEN}{division}{Style.RESET_ALL}")
            elif division < 0:
                print(f"El resultado de la división es: {Fore.RED}{division}{Style.RESET_ALL}")
            else:
                print(f"El resultado de la división es: {Fore.BLUE}{division}{Style.RESET_ALL}")

    case "resto":

        resto = numero_a % numero_b

        if resto > 0:
            print(f"El resto entre esos dos numeros es: {Fore.GREEN}{resto}{Style.RESET_ALL}")
        else:
            print(f"El resto entre esos dos numeros es: {Fore.BLUE}{resto}{Style.RESET_ALL}")

    case "potencia":

        potencia = numero_a ** numero_b

        if potencia > 0:
            print(f"El resultado de esa potencia es: {Fore.GREEN}{potencia}{Style.RESET_ALL}")
        elif potencia < 0:
            print(f"El resultado de esa potencia es: {Fore.RED}{potencia}{Style.RESET_ALL}")
        else:
            print(f"El resultado de esa potencia es: {Fore.BLUE}{potencia}{Style.RESET_ALL}")
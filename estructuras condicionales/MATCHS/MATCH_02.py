# Un sistema ofrece el siguiente menú: 

# 1 - Consultar saldo 
# 2 - Depositar dinero 
# 3 - Extraer dinero 
# 4 – Salir 

# El programa debe pedir al usuario que ingrese una opción y mostrar el mensaje correspondiente. 
# Utilizar un solo print, y pintar con colorama cada una de las opciones con un color diferente. 
from colorama import Fore, Style, init
init()


print(f"{Fore.RED}1 - Consultar saldo.\n{Fore.BLUE}2 - Depositar dinero. {Fore.CYAN}\n3 - Extraer dinero. {Fore.GREEN}\n4 - Salir.{Style.RESET_ALL}")

opcion_del_menu = int(input("Ingrese una opción del 1 al 4: "))

match opcion_del_menu:
    case 1:
        print(f"{Fore.RED}Consultar saldo.")
    case 2:
        print(f"{Fore.BLUE}Depositar dinero.")
    case 3:
        print(f"{Fore.CYAN}Extraer dinero.")
    case 4:
        print(f"{Fore.GREEN}Saliendo.")
    case _:
        print(f"{Fore.YELLOW}Opción inválida.")
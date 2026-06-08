# 10. Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado. 
# Determinar si el empleado debe o no pagar el impuesto a las ganancias.
# El mismo no se pagará si el empleado es casado con hijos y sus ingresos son menores a $2200000. 

sueldo = float(input("Ingrese un sueldo: "))
estado_civil = input("Ingrese estado civil(casado/soltero): ")
cantidad_de_hijos = int(input("Ingrese cuantos hijos: "))

if estado_civil == "casado" and cantidad_de_hijos > 0 and sueldo < 2200000:
    print("No deberá pagar impuesto a las ganancias.")
else:
    print("Debe pagar impuesto a la ganacia.")
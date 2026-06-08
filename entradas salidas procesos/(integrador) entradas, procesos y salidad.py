''' 
La juguetería El MUNDO DE BOBBY nos encarga un programa para conocer qué 
cantidad de materiales se necesitan para la fabricación de distintos juguetes. 

CONFECCIÓN DE UN COMETA:

Medidas: 

AB = Diagonal mayor 

DC = Diagonal menor 

BD y BC = lados menores 

AD y AC = lados mayores 


El usuario ingresará las medidas  BC, CD y DA. 


Detalles de construcción:
Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico 
y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa. 

El cometa estará construido con papel de alta resistencia. 
La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo. 

Necesitamos saber cuántos Mt de varillas de plástico y cuántos de papel son necesarios para la construcción 
en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cm.

'''

lado_menor_BC_cm = float(input("Ingrese la medida del lado menor del barrilete (Cm): "))

#Lado mayor DA = AC 
lado_mayor_DA_cm = float(input("Ingrese la medida del lado mayor del barrilete (Cm): "))

diagonal_menor_CD_cm = float(input("Ingrese la diagonal menor(Cm): "))

#Yo sé que con la diagonal menor CD, el lado menor BC y el lado mayor AC, tengo 2 triangulos rectángulos. Si yo divido 
# a CD en dos, consigo un catéto de esos rectángulos. con esos datos y haciendo pitágoras puedo sacar la diagonal mayor BA. 

#por ejemplo, agarro BC, y junto con la mitad de CD puedo sacar una parte de AB, la cual llamaré. mitad superior AB.

mitad_superior_diagonal_AB = (lado_menor_BC_cm**2 -(diagonal_menor_CD_cm/2)** 2)** 0.5

#ahora saco la otra mitad de la diagonal mayor:

mitad_inferior_AB = (lado_mayor_DA_cm**2 - (diagonal_menor_CD_cm/2)** 2)** 0.5

#por ultimo las sumo

diagonal_mayor_AB_cm = mitad_inferior_AB + mitad_superior_diagonal_AB

#calculo el perimetro del barrilete:

perimetro_barrilete = lado_mayor_DA_cm *2 + lado_menor_BC_cm *2 

#calculo la cantidad de metros de varrillas necesito

cantidad_de_metros_varillas = (perimetro_barrilete + diagonal_mayor_AB_cm + diagonal_menor_CD_cm)/100
metros_totales_de_varillas = cantidad_de_metros_varillas * 10
print(f"La cantidad de metros de varillas necesarios para 10 barriletes que necesito es de: {metros_totales_de_varillas} m.")

#ahora saco el área para cálcular el papel

area_barrilete_cm2 = (diagonal_mayor_AB_cm * diagonal_menor_CD_cm) / 2

cola_barrilete = area_barrilete_cm2 * 0.10

papel_para_un_barrilete = (cola_barrilete + area_barrilete_cm2) / 10000

total_papel_m2 = papel_para_un_barrilete * 10 

print(f"La cantidad de papel para los 10 barriletes con sus colas es de: {total_papel_m2} m2")
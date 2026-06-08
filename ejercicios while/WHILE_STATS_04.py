# 4. Mostrar la suma de los números pares desde el 1 hasta el 10. 

repeticiones = 0

suma_pares = 0

while repeticiones <= 10: 
    if repeticiones % 2 == 0:
        suma_pares += repeticiones

    repeticiones += 1
    
print(suma_pares)

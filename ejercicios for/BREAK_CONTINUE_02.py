# 2. Recorrer números del 1 al 100. Ignorar los múltiplos de 3. 
# Si aparece un el numero 77, detener el ciclo. Mostrar los números que si se imprimen.


for i in range(1, 101, 1):
    if i % 3 == 0:
        continue
    if i == 77: 
        break
    print(i)

    
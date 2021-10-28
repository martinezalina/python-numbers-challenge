import numpy as np  

print()
print('Hola! Bienvenidos a esta mini app.')
print()
print('Fase 1: A continuación vamos a pedir que ingresen la cantidad de números que deseen. Para finalizar ingresen -1.')
print('Fase 2: Vamos a brindarle el promedio de la secuencia y, el promedio de los valores mayores al promedio de la secuencia.')
print()
print('Comencemos ;)')
print()

val = 0
secuence = []

while (val != "-1"):
    val = input("Ingresar número: ")
    try:
        if (val != "-1"):
            secuence.append(int(val))
    except:
        print("Oooops... Recuerda agregar números.")

if secuence:
    print('La secuencia ingresada es', secuence)

    secuence_mean = np.mean(secuence)  
    print('El promedio de la secuencia es', secuence_mean)

    redux = []
    for a in secuence:
        if a > secuence_mean:
            redux.append(a)
    
    if redux:
        redux_mean = np.mean(redux)  
        print('El promedio de los valores mayores al promedio de la secuencia es', redux_mean)
    else: 
        print('Ningún número cumplió la condición como para obtener el promedio de los valores mayores al promedio de la secuencia')
else:
    print('Mmmm... parece que no ingresaste ningún número.')

import numpy as np  

def myfunction(l,x):
    print('La lista recibida es',l)
    print('El número recibido es',x)
    nums = []
    first = True

    for a in l:
        for b in l:
            c = a + b
            discance = abs(x - c)
            # print(a ,'+',b,'=',c,' -> distance =',discance)
            if not first:
                if discance < discance_selected:
                    a_selected = a
                    b_selected = b
                    discance_selected = discance
            else:
                a_selected = a
                b_selected = b
                discance_selected = discance
                first = False
            
    nums.append(a_selected)
    nums.append(b_selected)
    return nums


print()
print('Hola! Bienvenidos a esta mini app.')
print()
print('A continuación utilizaremos una función que recibe como parámetro una lista y un número x')
print('La función devolverá el par de números, cuya suma es más cercana al valor de x.')
print()


l = [0, 22, 28, 29, 30, 40]
x = 54

result = myfunction(l,x)

print('Los números seleccionados son', result)
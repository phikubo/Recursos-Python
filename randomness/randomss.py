import numpy as np
import matplotlib.pyplot as plt
import time
print("inicio del programa")

import random
#random.choice() escoje de posibilidades dadas una.
print("valor del dado: ",random.choice([1,2,3,4,5,6]))
#lo siguiente produce el mismo resultado
print("valor del dado: ",random.choice(range(1,7)))

print("----------------------------")
print("El problema del dado")
'''Supongamos que tenemos tres dados de 6,8 y 10 caras. Y solo
tengo la posibilidad de escoger uno y lanzarlo'''
dados=[range(1,7),range(1,9), range(1,11)]
print(dados)
#voy a escoger un dado de tres posibles:
eleccion_dado=random.choice(dados)
print(eleccion_dado) #esta variable es un tipo de dato range() pero no contiene algun valor, hasta que se llame.
#con el dado, ahora lo lanzo y obtengo el resultado:
print("del dado ", eleccion_dado, "obtengo ", random.choice(eleccion_dado))

print("----------------------------")
print("suma aleatoria")
'''Which of the following lines of code takes the sum of 10 random integers between 0 and 9?
'''
a=sum(random.choice(range(10)) for i in range(10))
print(a)

















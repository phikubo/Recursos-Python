import numpy as np
import matplotlib.pyplot as plt
import time
import random
print("inicio del programa")

#ejemplo1
'''
#Ejemplo de dados en n oportunidaes
#dentro del array, crea una lista en 10 oportunidades con el valor del dado.
rolls=np.array([random.choice([1,2,3,4,5,6]) for i in range(1000000)])
print(len(rolls))
plt.hist(rolls, bins=np.linspace(0.5,6.5,7))
'''
    
#ejemplo 2
'''
Suponga que tiene 10 dados  los lanza. Suma todos los resultados.
Ahora hace eso 10,100, y 1000 veces.
Como los experimentos de probabilidad!

rolls=np.array([random.choice([1,2,3,4,5,6]) for i in range(10)])
print(sum(rolls), rolls) #lanzo el dado 10 veces y sumo los valores.
lanzar10_veces=np.array([sum(np.array([random.choice([1,2,3,4,5,6]) for i in range(10)])) for i in range(10000)])
print(min(lanzar10_veces), max(lanzar10_veces), len(lanzar10_veces))
plt.grid(True)
plt.title("Histogram with 'auto' bins, aprox to normal dist")
plt.hist(lanzar10_veces, bins=91)
'''

#ejemplo 3
	#crear numero aleatorio:
print(np.random.random())
	#crear n numeros aleatorios:
print(np.random.random(4))

	#crear arrays con dimension random( (rows, columns)<-tupla ):
print(np.random.random((4,5)))
	
	#crear valores de la distribucion normal normal(mean, deviation):
print(np.random.normal(0,1, 10))
	#crear arrays de dimension n ( (matrix, rows, colums) ):
print(np.random.normal(0,1, (2,4,6)))

#ejemplo 4, 
	#el mismo que ejemplo 2, rows->numero de dado (1 entre 10), colums->numero de lanzamientos
rolls=np.random.randint(1,7, (10,3))
print(rolls, rolls.shape, np.sum(rolls, axis=1)) #axis para sum, puede ser 0 para colums, o 1 para rows

#ahora si desarrolamos el ejemplo
rolls4=np.random.randint(1,7,(1000000,10))
sumrolls=np.sum(rolls4, axis=1)
plt.hist(sumrolls)


plt.show()
















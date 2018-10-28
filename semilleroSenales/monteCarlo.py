# Kling, Ronn. Learning DEAP from examples.
 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import array
import random
import numpy as np
import math

##x= hacer 1000 veces la toma de un numero de 1:6.
#Creamos matriz de ceros, con el tamañano de x
#hacemos ciclo for: 1:len(r)
# si, x[3] ==3 o x[6]==6,
	#R[k]=1
	#o R[k]=0
#

'''
rolls=np.array([random.choice([1,2,3,4,5,6]) for i in range(1000000)])
matriz_ceros=np.zeros(len(rolls))

for i in range(1,len(rolls)):
	if rolls[i]==3 or rolls[i]==6:
		matriz_ceros[i]=1
	else:
		matriz_ceros[i]=0

probabilidad=sum(matriz_ceros)
print(probabilidad/len(rolls))
cumulativesum=np.zeros(len(rolls))
'''

'''
#X>1 AND y>1, X>1 or Y>1, max{X,Y}<=1
X=np.random.normal(0,1,10000)
Y=np.random.normal(0,1,10000)
matriz_cerosxy=np.zeros(len(X))

for i in range(len(X)):
	#if X[i]>1 and Y[i]>1:
	if np.maximum(X[i],Y[i])<=1:
		matriz_cerosxy[i]=1
	else:
		matriz_cerosxy[i]=0
pr2=sum(matriz_cerosxy)
print(pr2/len(X))

'''

'''

#calculo de integrales definidas

#func=sin(X)

x=np.random.uniform(0,math.pi,10000) #por que va desde 0 a pi
y=np.random.rand(10000)	#por que en y va hasta 1
#y=np.random.uniform(0,1,10000) #corregir lo anterior por que salen numeros por fuera de 1
matriz_cerossin=np.zeros(len(x))
for i in range(len(x)):
	if y[i]<=math.sin(x[i]):
		matriz_cerossin[i]=1
	else:
		matriz_cerossin[i]=0

pr3=sum(matriz_cerossin)
print((pr3*math.pi/len(x)))
#==>> h(b-a), h=1, b=pi, a=0
'''

'''
#integral(-20,20) de sinc(t/2)
# h=1, b=20, a=-20

x=np.random.uniform(-20,20,10000) #por que va desde 0 a pi
y=np.random.rand(10000)	#por que en y va hasta 1
matriz_cerossin=np.zeros(len(x))
for i in range(len(x)):
	if y[i]<=np.sinc(x[i]/2)**2:
		matriz_cerossin[i]=1
	else:
		matriz_cerossin[i]=0
pr3=sum(matriz_cerossin)
print((pr3*40/len(x)))
'''



#volumen triangular dentro de un cubo

x=np.random.rand(10000) #por que va desde 0 a 1
y=np.random.rand(10000) #por que va desde 0 a 1
z=np.random.rand(10000) #por que va desde 0 a 1

#x=np.random.uniform(0,1,10000)
#y=np.random.uniform(0,1,10000)
#z=np.random.uniform(0,1,10000)

matriz_cerossin=np.zeros(len(x))

for i in range(len(x)):
	if y[i]<=1-x[i] and z[i]<=1-x[i]-y[i]:
		matriz_cerossin[i]=1
	else:
		matriz_cerossin[i]=0

pr4=sum(matriz_cerossin)
print((pr4/len(x)))



















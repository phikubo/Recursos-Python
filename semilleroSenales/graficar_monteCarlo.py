#por Michael M. Tenorio
import random
import numpy as np
import matplotlib.pyplot as plt

#volumen triangular dentro de un cubo
x=np.random.rand(10000) #por que va desde 0 a 1
y=np.random.rand(10000) #por que va desde 0 a 1
z=np.random.rand(10000) #por que va desde 0 a 1
matriz_cerossin=np.zeros(len(x))

for i in range(len(x)):
	if y[i]<=1-x[i] and z[i]<=1-x[i]-y[i]:
		matriz_cerossin[i]=1
	else:
		matriz_cerossin[i]=0

sumatoria_binaria=sum(matriz_cerossin)
resultado=sumatoria_binaria/len(x)
cumulativa=np.cumsum(matriz_cerossin)
ejex=np.arange(1,len(x)+1)
graficar=cumulativa/ejex
#graficar
plt.grid(True)
plt.plot(ejex, graficar)
plt.show()

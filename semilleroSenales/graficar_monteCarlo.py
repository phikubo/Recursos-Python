#por Michael M. Tenorio
import random
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing
import time

def procesar(matriz_cerossin):
	x=np.random.rand(1000000) #por que va desde 0 a 1
	y=np.random.rand(1000000) #por que va desde 0 a 1
	z=np.random.rand(1000000) #por que va desde 0 a 1
	matriz_cerossin=np.zeros(len(x))
	for i in range(10):
		if y[i]<=1-x[i] and z[i]<=1-x[i]-y[i]:
			matriz_cerossin[i]=1
		else:
			matriz_cerossin[i]=0
	return matriz_cerossin


def montecarlo():
	p=[]
	x=np.random.rand(1000000)
	matriz_cerossin=np.zeros(len(x))
	with multiprocessing.Pool() as pool:
		pool.map(procesar, matriz_cerossin)
	#procesar(matriz_cerossin)

	sumatoria_binaria=sum(matriz_cerossin)
	resultado=sumatoria_binaria/len(x)
	cumulativa=np.cumsum(matriz_cerossin)
	ejex=np.arange(1,len(x)+1)
	graficar=cumulativa/ejex
	#graficar
	#plt.grid(True)
	#plt.plot(ejex, graficar)
	#plt.show()




if __name__ == "__main__":
	print("Calculando el volumen de un cubo con montecarlo, un momento...")
	#volumen triangular dentro de un cubo
	

	#x=np.random.rand(100000) #por que va desde 0 a 1
	#y=np.random.rand(100000) #por que va desde 0 a 1
	#z=np.random.rand(100000) #por que va desde 0 a 1
	#p=[x,y,z]

	time.sleep(1)
	start_time = time.time()
	montecarlo()


	#with multiprocessing.Pool() as pool:
	#	pool.map(montecarlo, p)

	duration = time.time() - start_time
	print(f"Duration {duration} seconds")
else:
	print("imported")

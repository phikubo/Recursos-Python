import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from distanciaDosPuntos import distancia


def encontrar_distancias(origen, vecinos):
	"""Retorna las distancias"""
	distancias = np.zeros(puntos.shape[0])
	for i in range(len(distancias)):
		distancias[i]=distancia(origen, vecinos[i])
		print("puntos: ",vecinos[i] , "en ", i, "distancias: ", distancias[i])
	return distancias

def encontrar_vecino(origen, vecinos, k=3):
	"""Encuentra los primeros k vecinos mas cercanos usando la funcion sorted"""
	distancias = np.zeros(puntos.shape[0])
	for i in range(len(distancias)):
		distancias[i]=distancia(origen, vecinos[i])
		print("puntos: ",vecinos[i] , "en ", i, "distancias: ", distancias[i])
	ind= np.argsort(distancias)
	return ind[:k]

def calcular_knn(origen, vecinos):
	"""Calcula segun la distancia si pertenece a una clase u otra"""
	pass
	
		
if __name__=="__main__":
	#vector columna: array([ [a0,b0], [a1,b1], [a2,b2] , ..., [an,bn]   ])
	#si fuera de mas dimesiones en filas:
	#array([ [a0,b0, c0, ..., z0], [a1,b1,c1,...,z1] , ... , [an,bn,cn,...,zn]   ]) 
	puntos=np.array([ [1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3] ])
	punto_arbitrario= np.array([2.5,2])
	print(puntos.shape[0], len(puntos)) #shape[dimension], 0: columna, 1 para fila, equivalente a len(). 
	#Shape lo hace tambien en filas, len no.
	
	distancias = np.zeros(puntos.shape[0])
	
	distancias=encontrar_distancias(punto_arbitrario, puntos)
	indx_k_vecinos_cercanos = encontrar_vecino(punto_arbitrario, puntos)
	#argsort, regresa el index de las distancias de menor a mayor en valor.
	sorteadas=np.argsort(distancias)
	minima_distancia=min(distancias)
	print("minima distancia: ", minima_distancia)
	print("distancias sorted: ", sorteadas)
	plt.figure()
	plt.grid(True)
	plt.hist(distancias)
	plt.hist(distancias,density=True, cumulative=True, histtype="step")
	plt.figure()
	plt.grid(True)
	plt.plot(distancias, "r-")
	print(puntos)
	print("longitud array: ",len(puntos))
	print("Primera posicion: ", puntos[0], "segunda posicion: ", puntos[1])
	print(  "En la segunda posicion, adentro el segundo valor: ",puntos[1][1])
	print(puntos[:3]) #Hasta la n posicion: array[:n] ->1,2,3,...,n
	print(puntos[:,1]) #vector columna posicion k: array[:,k]
	#para entenderlo seria: : -> logitud del vector; :,1->la columa, entonces
	#array[<Para todo el vector>(:)<,> <la k columna>(1,k=1)]: array[: , k=1]
	
	print("indices ", indx_k_vecinos_cercanos, "puntos : ",puntos[indx_k_vecinos_cercanos])
	
	#circulo de tipo patch, clase por defecto de matplotlib para hacer poligonos
	fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
	circle = patches.Circle((punto_arbitrario[0],punto_arbitrario[1]), radius=minima_distancia)
	circle2 = patches.Circle((2,2), radius=minima_distancia, facecolor="none", edgecolor="g")
	ax.add_patch(circle)
	ax.add_patch(circle2)
	
	#alternativa para el circulo, de forma manual:
	#En este caso, radio=0.5; 2.5 y 2 son lo que hay que sumar para ubicar el circulo al centro del punto_arbitrario.
	#una formula general seria:
	#>>plot(radio*seno(theta) +desplazamiento_en_x, radio*coseno(theta) +desplazamiento_en_y, "color")
	theta = np.linspace(-np.pi, np.pi, 200)
	plt.plot(0.5*(np.sin(theta))+2.5, 0.5*(np.cos(theta))+2, "k-")
	
	
	#LATER ON, Search for the colorbar, how to implement it.
	#cbar =fig.colorbar(ax)
	#cbar.solids.set_edgecolor("face")
	#draw()
	
	plt.plot(puntos[:,0], puntos[:,1], "ro")
	plt.plot(punto_arbitrario[0],punto_arbitrario[1], "bo")
	plt.grid(True)
	plt.show()

	
else:
	print("modulo importado","Caso 3: KNN")


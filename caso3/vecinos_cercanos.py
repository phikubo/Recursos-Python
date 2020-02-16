import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from distanciaDosPuntos import distancia
from calculadora import contar_votos_scipy
import scipy.stats as ss

#no se implementa formalmente
def encontrar_distancias(origen, vecinos):
	"""Retorna las distancias"""
	distancias = np.zeros(puntos.shape[0])
	for i in range(len(distancias)):
		distancias[i]=distancia(origen, vecinos[i])
		print("puntos: ",vecinos[i] , "en ", i, "distancias: ", distancias[i])
	return distancias

def encontrar_vecino(origen, vecinos, k=3):
	"""Encuentra los primeros k vecinos mas cercanos usando la funcion sorted"""
	distancias = np.zeros(vecinos.shape[0])
	for i in range(len(distancias)):
		distancias[i]=distancia(origen, vecinos[i])
		print("puntos: ",vecinos[i] , "en ", i, "distancias: ", distancias[i])
	ind= np.argsort(distancias)
	return ind[:k]

	#origen:punto de origen, vecinos: puntos vecinos, salida: clase_binaria
def calcular_knn(origen, vecinos, salida, k=5):
	"""Calcula segun la distancia si pertenece a una clase u otra, de forma binaria"""
	indices_cercanos=encontrar_vecino(origen, vecinos, k)
	resultado=contar_votos_scipy(salida[indices_cercanos])
	print(resultado)
	return contar_votos_scipy(salida[indices_cercanos])

def generar_datos(m=30):
	"""Crea dos conjuntos de datos usando distribucion bivariate normal """
	puntos_sinteticos_clase_cero = ss.norm(0,1).rvs((m,2))
	puntos_sinteticos_clase_uno = ss.norm(1,1).rvs((m,2))
	coordenadas_puntos=np.concatenate( (puntos_sinteticos_clase_cero,puntos_sinteticos_clase_uno), axis=0 )
	clase_binaria_m = np.concatenate( (np.repeat(0,m),np.repeat(1,m) ) ) 
	return (coordenadas_puntos, clase_binaria_m) #puntos, salida
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
	print(puntos)
	print("longitud array: ",len(puntos))
	print("Primera posicion: ", puntos[0], "segunda posicion: ", puntos[1])
	print(  "En la segunda posicion, adentro el segundo valor: ",puntos[1][1])
	print(puntos[:3]) #Hasta la n posicion: array[:n] ->1,2,3,...,n
	print(puntos[:,1]) #vector columna posicion k: array[:,k]
	#para entenderlo seria: : -> logitud del vector; :,1->la columa, entonces
	#array[<Para todo el vector>(:)<,> <la k columna>(1,k=1)]: array[: , k=1]
	
	print("indices ", indx_k_vecinos_cercanos, "puntos : ",puntos[indx_k_vecinos_cercanos])
	
	
	#clase binaria sirve para identificar dos clases
	clase_binaria=np.array([0,0,0,0,0,-1,-1,-1,-1])
	
	#como se clasifica segun clase binaria, el resultado es 0 o 1.
	print("Clase binaria test")
	punto_arbitrario_de_prueba=np.array([1.0, 2.7])
	resultado_cercanos, veces = calcular_knn(punto_arbitrario_de_prueba, puntos, clase_binaria)
	print("gano la clase: ", resultado_cercanos, "con ", veces, "votos")
	
	#Generar Synthetic Data en reemplazo de Clase_binaria:
	#norm es una variable aleatoria normal y continua, definida como:
	#>> modulo.norm(params).rvs( (filas, columas) )
	puntos_sinteticos_clase_cero = ss.norm(0,1).rvs((5,2))
	puntos_sinteticos_clase_uno = ss.norm(1,1).rvs((5,2))
	
	#unimos las dos clases en un solo vector
	#axis los apila en 0 en la misma columna ( : ) y 1 los separa en diferentes columnas ( . .)
	# (:) y (..) indican la forma de apilar, siendo los puntos los vectores
	datos_sinteticos=np.concatenate( (puntos_sinteticos_clase_cero,puntos_sinteticos_clase_uno), axis=0 )
	print("1: ",puntos_sinteticos_clase_cero )
	print("2 ", puntos_sinteticos_clase_uno)
	print("3",datos_sinteticos)
	#la funcion genera tantos puntos a plotear como salidas. 
	
	#numpy.repeat( (numero a repetir, veces a repetir) )
	l=3
	clase_binaria_k = np.concatenate( (np.repeat(0,l),np.repeat(1,l) ) ) 
	print(clase_binaria_k)
	
	#Testeo
	print("prueba de funcion generar_datos o mas bien, generar conjunto de puntos")
	m=10
	(puntos_aleatorios, salida)= generar_datos(m)
	
	
	
	
	print("Fin")
	#------------------GRAFICAS
	
	#histograma y comulativa
	plt.figure()
	plt.grid(True)
	plt.hist(distancias)
	plt.hist(distancias,density=True, cumulative=True, histtype="step")
	plt.figure()
	plt.grid(True)
	plt.plot(distancias, "r-")
	
	#grafia de puntos aleatorios:
	plt.figure()
	plt.grid(True)
	#>>puntos[0:n, 0] y puntos[0:n,1], indica que se recorre el vector hasta n en la columna 0 y luego la 1
	#Se recorre hasta n por que hasta ahi va el primer set de puntos, luego, puntos[:n, 0] y puntos[:n,1]
	#indica que se recorre hasta el final en la columna 0 y 1, dado que el vector tiene logitud 2n.
	plt.plot(puntos_aleatorios[:m,0],puntos_aleatorios[:m,1], "ro")
	plt.plot(puntos_aleatorios[m:,0],puntos_aleatorios[m:,1], "bo")
		
	#circulo de tipo patch, clase por defecto de matplotlib para hacer poligonos
	#circulo es el radio de alcance de el vecino mas cercano
	#circulo2 es un circulo de prueba sin relleno.
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
	
	#hexagono
	#1, 6, 12, 18, 24, ++6

else:
	print("modulo importado","Caso 3: KNN")


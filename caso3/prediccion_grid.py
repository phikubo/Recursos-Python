import calculadora as calc
import distanciaDosPuntos as ddp
import vecinos_cercanos as vc
import numpy as np
import matplotlib.pyplot as plt
from plot_prediction_grid import plot_prediction_grid
import time
 
#numpy.arrange(inicio, final, pasos), 
#crea un vector espaciado simetricamente en pasos desde el inicio hasta el final del valor dado


def crear_prediccion_grid(vecinos, salida, limites, h, k):
	"""Clasifica cada punto en la grid de prediccion"""
	(x_min,x_max, y_min, y_max) = limites
	xs=np.arange(x_min, x_max, h)
	ys=np.arange(y_min, y_max, h)
	xx, yy = np.meshgrid(xs,ys)
	#por el tamaño de h hay 70 numeros espaciados entre los limites
	print("matriz: ", xx.shape, "iteraciones a hacer: ", xx.shape[0]*xx.shape[1])
	time.sleep(5)
	print("iniciando!")
	time.sleep(1)
	prediccion_grid = np.zeros(xx.shape, dtype=int)
	contador=0
	#por cada punto, se compara la distancia a todos los demas
	for i,x in enumerate(xs):
		for j,y in enumerate(ys):
			contador+=1
			punto= np.array([x,y])
			print("------------> ", contador)
			prediccion_grid[j,i]=vc.calcular_knn(punto, vecinos, salida, k)
	return xx,yy, prediccion_grid

if __name__ == "__main__":
	print("Caso 3: grilla de prediccion")
	m=30
	#m es la cantidad de puntos a generar
	(puntos_aleatorios, clase_binaria)= vc.generar_datos(m)
	plt.grid(True)
	plt.plot(puntos_aleatorios[:m,0],puntos_aleatorios[:m,1], "ro")
	plt.plot(puntos_aleatorios[m:,0],puntos_aleatorios[m:,1], "bo")
	#k indica la presicion, entre mas cerca de 1, mas preciso.
	#aclaracion: aunque k si representa la presicion de la clasificacion de la grilla, segun la teoria, por BIAS VARIANCE TRADE-OFF
	#que sea mas cercano a 1 no indica mayor presicion si no un valor intermedio
	k=4; nom_archivo="knn_grid_k_4.pdf";limites=(-3,4, -3,4); h=0.1
	#la cantidad de iteraciones se debe a que <h> es un espaciado diminuto por lo que requiere mayor procesamiento.
	(xx,yy,prediccion_grid) = crear_prediccion_grid(puntos_aleatorios, clase_binaria, limites, h, k)
	plot_prediction_grid(xx,yy, prediccion_grid, nom_archivo, puntos_aleatorios, clase_binaria)
	#plt.show()
	
else:
	print("Modulo importado: Grilla de prediccion.")

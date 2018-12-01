import calculadora as calc
import distanciaDosPuntos as ddp
import vecinos_cercanos as vc
import numpy as np
import matplotlib.pyplot as plt

#numpy.arrange(inicio, final, pasos), 
#crea un vector espaciado simetricamente en pasos desde el inicio hasta el final del valor dado


def crear_prediccion_gri(vecinos, salida, limites, h, k):
	"""Clasifica cada punto en la grid de prediccion"""
	(x_min,x_max, y_min, y_max) = limites
	xs=np.arange(x_min, x_max, h)
	ys=np.arange(y_min, y_max, h)
	xx, yy = np.meshgrid(xs,ys)
	
	prediccion_grid = np.zeros(xx.shape, dtype=int)
	
	for i,x in enumerate(xs):
		for j,y in enumerate(ys):
			punto= np.array([x,y])
			prediccion_grid[j,i]=vc.calcular_knn(punto, vecinos, salida, k)
	return xx,yy, prediccion_grid

if __name__ == "__main__":
	print("Caso 3: grilla de prediccion")
	
else:
	print("Modulo importado: Grilla de prediccion.")

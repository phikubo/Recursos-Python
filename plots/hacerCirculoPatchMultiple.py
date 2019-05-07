#origen carpeta plots

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import numpy as np


def crear_circulos(puntos, radio):
	circulos=[]
	
	for i in puntos:
		circulos.append(patches.Circle( (i[0], i[1]), radius=radio ))
	return circulos

def agregar_al_patch(ax, circulos):
	for i in circulos:
		ax.add_patch(i)
		i.set_facecolor(np.random.rand(3))
	

def main():
	fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})
	ax.set_xlim(0, 10)
	ax.set_ylim(0, 10)
	k=1
	radio=1
	#generar puntos
	origenes=10*np.random.random((k,2))
	#crear circulos centrados en esos puntos
	circulos=crear_circulos(origenes,radio)
	
	agregar_al_patch(ax,circulos)
	
	plt.grid(True)
	plt.show()

	#MEDOTOLOGIA:
	#ensayar con la lista
	#ensayar con un for
	#ensayar con una funcion

if __name__ == "__main__":
	main()
else:
	print("modulo importado")




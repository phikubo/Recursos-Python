import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import math
def obtener_linea(angulos):
	ang_x=[]
	ang_y=[]
	for i in angulos:
		ang_x.append(math.cos(math.radians(i)))
		ang_y.append(math.sin(math.radians(i)))
	return ang_x, ang_y

def dibujar_circulo(radio,angulos):
	fig = plt.figure()
	ax = plt.axes()
	ax.set_aspect(1)
	angx,angy=obtener_linea(angulos)
	theta = np.linspace(-np.pi, np.pi, 200)
	plt.plot(radio*np.sin(theta), radio*np.cos(theta))
	for x,y in zip(angx, angy):
		plt.plot(radio*x,radio*y, 'r*')
	plt.grid(True)
	plt.show()
	
if __name__ == "__main__":
	radio=10
	angulos=[0, 90]
 
	dibujar_circulo(radio, angulos)
else:
	pass

import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
import math
import random
import time
import calculadora
#http://magomar.github.io/deludobellico//programming/java/hexagonal-maps/2013/10/10/mapas-hexagonales-2.html
#https://joseguerreroa.wordpress.com/2016/11/17/como-producir-rejillas-grid-hexagonales-mediante-pyqgis/
#https://gamedevelopment.tutsplus.com/es/tutorials/introduction-to-axial-coordinates-for-hexagonal-tile-based-games--cms-28820
#https://gamedevelopment.tutsplus.com/es/tutorials/hexagonal-character-movement-using-axial-coordinates--cms-29035
 
#modificado por: John Michael (phikubo)

'''La modificación consiste en que se puede escalar los hexagonos al radio que uno fije, en ese sentido
la grilla de hexagono mantiene su forma.
En la próxima entrega se hara sectorización (por 3) y se permitirá varios niveles (vueltas respecto al origen) en la grilla.''' 

#NOTA PERSONAL: Si colocar time.sleep(time) ubicar un print() que indique su existencia.

def calcular_radio_externo(radio):
	n=5
	#print(math.sin(30), math.radians(30), math.degrees(30))
	lado=radio*2*math.sin(math.radians(30))
	#print("lado", lado, radio)
	#radio_externo=radio+lado/2 #para una grilla horizontal
	radio_externo=radio+n*(radio/2)  #para una grilla vertical
	return radio_externo
	
def guardar_lista(lista,bd_coordenadas):
	#print("coordenadas: ",lista, "y ",lista[0],",", lista[1])
	#x+y+z=0 en coordenadas axiales, despejando z=-x-y entonces lo genero
	#en este caso x, y equivalen respectivamente a lista[0] y lista[1]
	coordenada_z = -lista[0]-lista[1]
	lista.append(coordenada_z)
	##print("coordenadas axial final: ",lista)
	bd_coordenadas.append(lista)
	#print(bd_coordenadas)
	return bd_coordenadas
	 
def generar_lista(nivel,rae, bd_coordenadas):
	#funcion que no se implementa por que es inutil
	for j in range(nivel):
		for m in range(nivel):
			
			l=[j,m]
			#print(l, type(l))
			guardar_lista(l, bd_coordenadas)
			#proceso
			#guardar
			#limpiar variable
			#volver a empezar
	


#coord = [[0,0,0],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1],[1,-1,0],[1,0,-1]]
#coordenadas cubicas ejes axiales para grilla hexagonales
#cual es la relacion entre el tres y el radio dos.
###coord = [[0,0,0],[0,3,-3],[-3,3,0],[-3,0,3],[0,-3,3],[3,-3,0],[3,0,-3]]
#cuales serían las coordenadas para una grilla mas grande. Existe algun algoritmo para sacar las 
#coordenadas de forma dinamica?. Que cada hexagono se ubique del centro hacia afuera y cada suma
#se ubique contra las manecillas del reloj.

#orden = [ [],[],[],[],[],[],[] ]
# Horizontal cartesian coords
##hcoord = [c[0] for c in coord]
 
# Vertical cartersian coords
##vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]
def crear_labels(coord):
	'''Asocia las coordenadas axiales con el numero de la celda, de ese modo crea en el orden una lista de coordenadas'''
	label=[]
	label_aux=[]
	coma="."
	str_aux=""
	conta=0
	for i in coord:
		#print("i: ",i )
		for j in i:
			#print(j)
			str_aux=str_aux+coma+str(j)
		##print("aux: ",str_aux)
		label_aux.append(str_aux)
		label.append(label_aux)
		str_aux=""
		label_aux=[]
	return label
	
#falta crear el algorimo de sectorizacion
def crear_color(coord):
	'''Crea una lista random de colores a partir de una lista core'''
	colores=["Green","Blue","Red"]
	label_aux=[]
	colors=[]
	#print(random.choice(colores))
	for i in range(len(coord)):
		color=random.choice(colores)
		label_aux.append(color)
		colors.append(label_aux)
		label_aux=[]
	return colors
		


def crear_coordenadas_grilla_horizontal(coord, coef, nivel):
	'''Calcula las coordenadas horizontales y verticales. En el caso de las coordenadas verticales se usa las primeras dos
	elementos de la lista para expandir la grilla'''
	#proceo 1 completado
	#hcoord = [coef*c[0] for c in coord] #para grilla horizontal
	hcoord = [1/3*coef*c[0] for c in coord]
	vcoord =[]
	vc_aux=[]
	coordenadas_pares=[]
	coordenadas_impares=[]
	coordenadas=[]
	n=nivel*nivel
	#proceso vertical
	
	for i in range(2*nivel):
		coordenadas.append(coord[i])
	'''	
	for i in range(nivel):
		coordenadas_pares.append(coord[i])
	
	for i in range(nivel,2*nivel):
		coordenadas_impares.append(coord[i])
	print("coordenadas pares ",coordenadas_pares)
	print("coordenadas impares ",coordenadas_impares)
	print("coordenadas por nivel ",coordenadas )
	'''
	for c in coordenadas:
		resultado=-1*2. * np.sin(np.radians(120)) * (coef*c[1] - coef*c[2]) /3.
		vc_aux.append(resultado)
	vcoord=calculadora.calc_rango(2*nivel)*vc_aux
	vcoord=vcoord[0:n]
	#print(len(vcoord),  n  )
	#print("por dos", vcoord[0:n])
	return hcoord, vcoord
	 
 	
			
			
def plotear_grid(coef,radio, coord, nivel):
	'''Plotea graficas de celdas hexagonales'''
	# Horizontal cartesian coords	 
	##hcoord = [coef*c[0] for c in coord]
	 
	labels=crear_labels(coord) 
	colors=crear_color(coord)
	##print("labels: ",labels )
	# Vertical cartersian coords
	#calcula el centro de los hexagonos
	hcoord, vcoord = crear_coordenadas_grilla_horizontal(coord, coef, nivel)
	
	####cordenada x pares arriba, impares abajo
	##vcoord = [-1*2. * np.sin(np.radians(60)) * (coef*c[1] - coef*c[2]) /3. for c in coord]
	
	##print("coordenadas vcord", vcoord )
	 
	#el numero de colores debe ser igual a len(coord)
	
	fig, ax = plt.subplots(1)
	ax.set_aspect('equal')
	vertical_coef=1.154
	vertical_coef=1
	
	print(len(hcoord), len(vcoord))
	
	for x, y, c, l in zip(hcoord, vcoord, colors, labels):
		color = c[0].lower()  # matplotlib understands lower case words for colours
		hex = RegularPolygon((x, y), numVertices=6, radius=vertical_coef*radio, #0.67
                         orientation=np.radians(30), #con 60 grados funciona perfecto, pero las coordenadas cambian. Antes 30
                         facecolor=color, alpha=0.2, edgecolor='k')
                         #cambiar radius=2. / 3. , cuando se usa coord_0
		ax.add_patch(hex)
    	# Also add a text label
		ax.text(x, y+0.2, l[0], ha='center', va='center', size=6)
	# Also add scatter points in hexagon centres
	ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)
	plt.grid(True)
	plt.savefig("hexagrid.png")
	plt.show()
 

if __name__ =="__main__":
	print("main")
	radio=10
	nivel=3
	bd_coordenadas=[] 
	#calcular_radio_externo(radio)
	rae=calcular_radio_externo(radio)
	coef=rae
	#plotear_grid(coef, radio)
	generar_lista(nivel, rae, bd_coordenadas)
	print(bd_coordenadas)
	plotear_grid(coef, radio, bd_coordenadas, nivel)
	
	'''1- Actualmente el algoritmo genera grillas simetricas. La idea es crear grillas n*n-1, nE{impares}
	
	'''
	'''2-La sectorización funciona para un nivel multiplo de 3. Funciona quiere decir que para los numeros
	impares, quedan celdas sin usar, por lo que no es eficiente producir celdas que no se usan'''
	
	
	
else:
	print("modulo importado")
 
 
  

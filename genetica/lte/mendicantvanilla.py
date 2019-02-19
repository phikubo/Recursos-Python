import matplotlib.pyplot as plt
#from matplotlib.patches import RegularPolygon
import numpy as np
import math
import random
import time
import calculadora
from hexagrid import hexagrid

if __name__ =="__main__":
	print("Mod. Cobertura")
	
	#------------------------------
	#PARAMETROS
	radio=100/10 #en decamentros
	nivel=1
	BS=1
	potencia=20
	tilt=10
	#no hay tipo de antena, solo horn
	potencia_w=potencia*10**3
	print(potencia_w,"Watios")
	
 
	#------------------------------
	#------------------------------
	print("Mendicant says Hello!")
		
	#plotea un circulo con puntos de azimut y radio.
	hexagrid(radio,nivel)
	zero_matrix=np.zeros((5,5))
	print("len", np.shape(zero_matrix))
	print(zero_matrix)
	#con el azimut dibuja los angulos respecto a una celda de radio radio
	

	'''Colocar el circulo en el centro de un solo bs'''
 
	
else:
	print("Modulo MendicantVanilla:cobertura importado.")
 
 
  

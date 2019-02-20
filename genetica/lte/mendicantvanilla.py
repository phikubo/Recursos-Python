import matplotlib.pyplot as plt
#from matplotlib.patches import RegularPolygon
import numpy as np
import math
import random
import time
import calculadora
from hexagrid import graficar
#import modelos
#from modelos import mod_perdida_ganancias as mpg
import modelos
import antenas
#https://www.thecodeship.com/patterns/guide-to-python-function-decorators/



#dimension n y dimension m hace referencia a la dimension de la matriz	
def iteracion(dim_m, dim_n):
	potencia_recibida = np.zeros(dim_n, dim_m)

def cobertura():
	radio = 100/10 #en decamentros
	nivel = 1
	bs = 1
	potencia = 20
	fr=1710
	tilt = 10
	sector = 3
	
	x_bs = 0.0
	y_bs = 0.0

	potencia_w = potencia*10**3
	azim = calculadora.azimut_lista(0)
	dim_m = (radio*bs)+((3*radio)/2) #25
	dim_n = (radio*bs)+((3*radio)/2) #25
	#matrices
	potencia_recibida = np.zeros((int(dim_n),int(dim_m)))
	dist_x = np.zeros((int(dim_n),int(dim_m)))
	dist_y = np.zeros((int(dim_n),int(dim_m)))
	print("longitud ", np.shape(potencia_recibida))

	#patron de antena, retorna at, y angulos
	at, theta_mod, A_theta, A_theta_dif = antenas.horn(tilt)

	#iteracion para cada sector.
	for i in range(sector):
		azimut=azim[i]
		print("azi ", azimut)
		#la jerarquia es incorrecta
		for j in range(1, int(dim_n)+1):
			dx = j*1.0 - x_bs
			print("dx ", dx)
			#print("time,,,")
			#time.sleep(1)
			for k in range(1,int(dim_m)+1):
				dy = k*1.0 - y_bs
				print("dy ", dy)
			#dist_x, dist_y, theta, freq, azim
				l, gan, theta, freq, d_km = modelos.mod_perdida_ganancias(dx, dy, theta_mod, fr, azimut)
				print(l, gan, theta, freq, d_km)

				#potencia recibida
				potencia_recibida[j-1][k-1] = 10*np.log10( potencia_w )+gan-l
		pot_rec_t = potencia_recibida.transpose()
	


if __name__ =="__main__":
	print("Mod. Cobertura")
	
	#------------------------------
	#PARAMETROS
	radio=100/10 #en decamentros
	nivel=1
	BS=1
	potencia=20
	tilt=10
	sector=3
	#no hay tipo de antena, solo horn
	potencia_w=potencia*10**3
	print(potencia_w,"Watios")
	
 
	#------------------------------
	#------------------------------
	print("Mendicant says Hello!")
	print("Time,,,")
	time.sleep(2)
		
	#plotea un circulo con puntos de azimut y radio.
	#graficar(radio,nivel)

	#-----------------------------------matrices de ceros
	zero_matrix=np.zeros((5,5))
	print("len", np.shape(zero_matrix))
	print(zero_matrix)
	cobertura()
	#con el azimut dibuja los angulos respecto a una celda de radio radio
 
	
else:
	print("Modulo MendicantVanilla:cobertura importado.")
 
 
  

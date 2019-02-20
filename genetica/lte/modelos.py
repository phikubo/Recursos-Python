import math
import time
import numpy as np
#math.radians(angle) #sirve para pasar de angulos a radianes.

def perdidas_espacio_libre(dist,freq):
	l=32.44+20*np.log10(dist)+20*np.log10(freq)
	return l

def ganancia_sectores(dist_x, dist_y, azim):
	theta_ue = math.atan(dist_y/dist_x)
	if dist_x < 0:
		theta_ue = theta_ue+math.pi
	if (azim - theta_ue - math.pi) < 0:
		theta_ue = theta_ue + 2*math.pi
	if theta_ue - azim - math.pi > 0:
		theta_ue = theta_ue - 2*math.pi
	rho = theta_ue - azim
	rho1 = (rho*180)/math.pi
	rho_60 = math.ceil(rho1) + 60
	return rho_60, rho

#funcion main
def mod_perdida_ganancias(dist_x, dist_y, theta, freq, azim):
	distancia= dist_x**2 + dist_y**2
	distan_km=distancia/100
	ganancia_max = 27

	l=perdidas_espacio_libre(distan_km,freq)
	rho_60, rho = ganancia_sectores(dist_x, dist_y, azim)
	gan = -1*np.minimum( (12* (rho_60/65)**2), 20) + ganancia_max
	return l, gan, rho_60, rho, distan_km

if __name__ == "__main__":
	print("Pruebas de modulo: Perdida de gananancias")
	a,b,c,d,e = mod_perdida_ganancias(5, 5, 0, 100, 0)
	print(a,b,c,d,e)
	print("Mod >>>>> OK")
else:
	print("modulo modelos importado")

import numpy as np


#en forma de funcion:
def distancia(p1,p2):
	"""Encuentra la distancia entre dos puntos dados"""
	return np.sqrt(np.sum(np.power(p2-p1, 2)))

if __name__=="__main__":
	#los valores entre corchetes son los valores del vector en si.
	punto1 = np.array([1,1]) 
	punto2 = np.array([4,4])
	print(punto1)
	print(punto2)
	#operacion resta, se hace posicion a posicion
	print("diferencia: ", punto2-punto1)
	#como el resultado es posicion a posicion, si elevo, se obtiene posicion a posicion la potencia:
	print("potencia: ", np.power(punto2-punto1, 2))
	#hago la suma interna:
	print("suma:", np.sum(np.power(punto2-punto1, 2)))
	# aplico ecuacion:
	print("raiz: ", np.sqrt(np.sum(np.power(punto2-punto1, 2))))
	d=distancia(punto1,punto2)
	print(d)
else:
	print("modulo importado","Caso 3: Distancia entre dos puntos")


import math
import time
def calc_rango(x):
	'''calcula el numero de celdas segun los pares e impares (x) que se le alimentan. Resulta que en hexagrid 
	para cada nivel solo se usan las primeras dos coordenadas: el primer par y el segundo impar. Pero el numero de
	celdas es nivel*nivel (eg. Para un nivel 4, las 8 primeras celdas, 4 impares y 4 pares, existen 16 celdas en total.
	De ese modo, es ineficiente calcular coordenadas, colores, etiquetas y demás, si se sobrepasa el numero de celdas.
	El numero exacto de celdas es calculado con esta funcion. '''
	n=0.25
	y=n*x**2
	#y=0.14*x+6.49
	return math.ceil(y)

if __name__ == "__main__":
	print("inicio")
	x=[1.,4.,6.,8.,10.,12.,14.,16.,18.]
	for i in x:
		#print(i, type(i))
		#time.sleep(5)
		
		print(i, " recta: ", calc_rango(i))
else:
	print("modulo ecuaciones importado")

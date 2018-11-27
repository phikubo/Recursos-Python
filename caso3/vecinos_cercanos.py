import numpy as np
import matplotlib.pyplot as plt


if __name__=="__main__":
	#vector columna: array([ [a0,b0], [a1,b1], [a2,b2] , ..., [an,bn]   ])
	#si fuera de mas dimesiones en filas:
	#array([ [a0,b0, c0, ..., z0], [a1,b1,c1,...,z1] , ... , [an,bn,cn,...,zn]   ]) 
	puntos=np.array([ [1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3] ])
	print(puntos.shape[0], len(puntos)) #shape[dimension], 0: columna, 1 para fila, equivalente a len(). Shape lo hace tambien en filas, len no.
	print(puntos)
	print("longitud array: ",len(puntos))
	print("Primera posicion: ", puntos[0], "segunda posicion: ", puntos[1], "En la segunda posicion, adentro el segundo valor: ",puntos[1][1])
	print(puntos[:3]) #Hasta la n posicion: array[:n] ->1,2,3,...,n
	print(puntos[:,1]) #vector columna posicion k: array[:,k]
	#para entenderlo seria: : -> logitud del vector; :,1->la columa, entonces
	#array[<Para todo el vector>(:)<,> <la k columna>(1,k=1)]: array[: , k=1]
	
	punto_arbitrario= np.array([2.5,2])
	plt.plot(puntos[:,0], puntos[:,1], "ro")
	plt.plot(punto_arbitrario[0],punto_arbitrario[1], "bo")
	plt.show()

	
else:
	print("modulo importado","Caso 3: KNN")


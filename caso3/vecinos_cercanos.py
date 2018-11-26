import numpy as np
import matplotlib.pyplot as plt


if __name__=="__main__":
	#vector columna: array([ [a0,b0], [a1,b1], [a2,b2] , ..., [an,bn]   ])
	#si fuera de mas dimesiones en filas:
	#array([ [a0,b0, c0, ..., i0], [a1,b1,c1,...,i1] , ... , [an,bn,cn,...,in]   ]) 
	puntos=np.array([ [1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3] ])
	print(puntos)
	print("longitud array: ",len(puntos))
	print("Primera posicion: ", puntos[0], "segunda posicion: ", puntos[1], "En la segunda posicion, adentro el segundo valor: ",puntos[1][1])
	print(puntos[:3]) #Hasta la n posicion: array[:n] ->1,2,3,...,n
	print(puntos[:,1]) #vector columna posicion k: array[:,k]
	#para entenderlo seria: : -> logitud del vector; :,1->la columa, entonces
	#array[<Para todo el vector>(:)<,> <la k columna>(1,k=1)]: array[: , k=1]
	
	p= np.array([2.5,2])
	#plt.plot(puntos[:,0], puntos[:,1], "ro")
	#plt.show()
else:
	print("modulo importado","Caso 3: KNN")


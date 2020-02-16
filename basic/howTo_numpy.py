import numpy as np

print("inicio del programa")

#definicion de vector con ceros

zero_vector=np.zeros(5)
zero_matrix=np.zeros((5,3)) #argumento como tupla, 2 dimensiones.

print(zero_vector, " es ", type(zero_vector))
print(zero_matrix, "es ",type(zero_matrix))
#traspuesta de A
A=np.array( [ [1,3],[5,9] ])
print(A, "transp: ", A.transpose())

x = np.array([1,2,5])
#x[1:2] da 2, por que, empieza en cero, pero no toma el ultimo valor.



#clase 15: indexin numpy arrays
print("------------------------")
z1=np.array([1,3,5,6,7,9])
z2=z1+1 #suma 1 a todos los elementos del array
print(z2)
indice=[1,3,4]
npindice=np.array([1,3,4]) 
print(z1[indice], z1[npindice]) #se obtiene las posiciones del array indicadas en la lista indice, o sea array.

#built in func
z=np.array([1,3,5,6,7,9])
print(z>6)#bool iterativo que retoran falso o verdadero si cumple la condicion
print(z[z>6]) #imprime los valores que cumplen la condicion

#cuidado con slicing:
zs=np.array([1,3,5,6,7,9])
w=zs[0:3]
print(w)
w[0]=11
print("w ",w, "zs: ",zs)
# lo anterior indica que al hacer ese tipo de slicing es como tomar un tramo espejo del array original.

#para obtener una copia no imagen del vector usamos indices:
zs1=np.array([1,3,5,6,7,9])
ind=np.array([0,1,2,3])
print(ind)
w=zs1[ind]
w[0]=11
print(w, "no modificado, ", zs1)

#clase 15: Building arrays
print("------------------------")
lins=np.linspace(0,100,10) #(inicio, final, numero de puntos linealmente distribuidos.
print(lins)

#ahora uno distribuido logaritmicamente:
logar=np.logspace(1,2,10) #(log10(inicio), log10(final), numero de puntos)
print(logar)

#ahora, por ejemplo si se decide tomar inicio=250 y final 500:
logar2=np.logspace(np.log10(250),np.log10(500),7)
print(logar2)

#Como saber el tamaño y numero de elementos presentes?
X=np.array([[1,2,3],[9,8,7]])
print("dimension ",X.shape, ", numero de elementos ",X.size)
#shape y size no son metodos son atributos del array por eso no tienen ()

#evaluar condiciones del array:
x=np.random.random(10)
prob=0.1
print("alguno es mayor ", np.any(x>prob))
print("todos son mayores ", np.all(x>prob))
print("x es ",x)

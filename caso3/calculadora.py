#print("Caso 3: calculadora")
import scipy.stats as ss
#modificando caso2/diccionario_de_palabras.py:
import random
def contar_votos(votos):
	"""
	Cuenta el numero de veces que esta el valor de un array. Funciona cuando hay empates (regresa ambos)
	"""
	votos_cuenta={}
	for voto in votos:
		if voto in votos_cuenta:
			votos_cuenta[voto] +=1
		else:
			votos_cuenta[voto] =1
	
	mayores=[]
	mayor_obtuvo=max(votos_cuenta.values())
	#items retorna la clave y el valor del diccionario
	for voto, cuenta in votos_cuenta.items():
		print(voto,cuenta)
		if cuenta == mayor_obtuvo:
			mayores.append(voto)
			print(mayores, "obtuvo la mayor cantidad de votos")
	return votos_cuenta, mayores, random.choice(mayores)
	
#import scipy.stats as ss
def contar_votos_scipy(votos):
	"""
	Cuenta el numero de veces que esta el valor de un array. Funciona cuando hay empates (regresa ambos)
	"""
	moda, cuenta= ss.mstats.mode(votos)
	return moda,cuenta
if __name__=="__main__":
	votos=[1,2,3,4,5,1,2,3,1,2,6,5,7,12,15,1,1,1,1,1,7,7,7,7,7,7,7]
	test,test2,test3=contar_votos(votos)
	print(test)
	print("maximo ",max(test))
	print("maximo de numeros",max(test.keys()))
	print("maximo de votos",max(test.values()))
	print("mayor ", test2, "eleccion de uno: ",test3)
	print("usando scipy ",contar_votos_scipy(votos))
else:
	print("modulo importado","Caso 3: calculadora")


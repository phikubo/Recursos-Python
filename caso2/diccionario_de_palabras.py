print("Caso 2")


texto="Esta es una cadena de prueba para evaluar aprendizaje del curso de edx de python para ciencias. Sin embargo, para incluir estas palabras seguidas de comas o puntos, hay que tratar diferente el problema."

def contar_palabras(texto):
	"""
	Cuenta cuantas veces esta una palabra en una cadena de texto
	"""
	texto=texto.lower()
	saltarse=[".",",",";",":","'",'"']
	for salto in saltarse:
		#Reemplaa salto con ""
		texto=texto.replace(salto,"")
		
	palabras_cuenta={}
	for palabra in texto.split(" "):
		if palabra in palabras_cuenta:
			palabras_cuenta[palabra] +=1
		else:
			palabras_cuenta[palabra] =1
	return palabras_cuenta



from collections import Counter
def contar_palabras_usando_modulo(texto):
	"""
	Cuenta cuantas veces esta una palabra en una cadena de texto usando modulos de python por defecto.
	"""
	texto=texto.lower()
	saltarse=[".",",",";",":","'",'"']
	for salto in saltarse:
		#Reemplaa salto con ""
		texto=texto.replace(salto,"")
	palabras_cuentas=Counter(texto.split(" "))
	return palabras_cuentas
		
print(contar_palabras(texto))
print(contar_palabras_usando_modulo(texto))

#comparamos
print("La comparación es: ")
print(contar_palabras(texto) == contar_palabras_usando_modulo(texto))

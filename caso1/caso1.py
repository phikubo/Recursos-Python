print("Caso 1")

#Tabla de traduccion, podria estar en un archivo.
tabla={
"ATA":"I","ATC":"I","ATT":"I","ATG":"M",
"ACA":"T","ACC":"T","ACG":"T","ACT":"T",
"AAC":"N","AAT":"N","AAA":"K","AAG":"K",
"AGC":"S","AGT":"S","AGA":"R","AGG":"R",
"CTA":"L","CTC":"L","CTG":"L","CTT":"L",
"CCA":"P","CCC":"P","CCG":"P","CCT":"P",
"CAC":"H","CAT":"H","CAA":"Q","CAG":"Q",
"CGA":"R","CGC":"R","CGG":"R","CGT":"R",
"GTA":"V","GTC":"V","GTG":"V","GTT":"V",
"GCA":"A","GCC":"A","GCG":"A","GCT":"A",
"GAC":"D","GAT":"D","GAA":"E","GAG":"E",
"GGA":"G","GGC":"G","GGG":"G","GGT":"G",
"TCA":"S","TCC":"S","TCG":"S","TCT":"S",
"TTC":"F","TTT":"F","TTA":"L","TTG":"L",
"TAC":"Y","TAT":"Y","TAA":"_","TAG":"_",
"TGC":"C","TGT":"C","TGA":"_","TGG":"W" }

def leer_secuencia(inputfile):
	"""Lee y regresa el contenido de un archivo sin caracteres especiales"""
	#referencia el archivo de nombre adn
	with open(inputfile,"r") as archivo:
		#sube el contenido a una variable
		secuencia2=archivo.read()
		#Se reemplaza los caracteres en la nueva variable
		secuencia=secuencia2.replace("\n","")
		secuencia=secuencia.replace("\r","")
		return secuencia

def traducir(sec, tabla=tabla):
	"""Traduce una secuencia nucleotica en una cadena de amino acidos, solo si la secuencia es multiplo de 3"""
	proteina=""
	if len(sec) % 3 ==0:
		#el numero de caracteres es divisible por 3, por tanto
		#si se puede traducir
		#range(inicio, final, cantidad por pasos)
		
		#loop sobre la secuencia
		for i in range(0,len(sec),3):
			#extraer un codon o triada
			triada = sec[i:i+3]
			#se busca el valor de la triada en el diccionario
			#y se va concatenando:
			proteina += tabla[triada]
		return proteina
	else:
		print("No valido", len(sec))
		return proteina


#______________________main_______________

#abre los archivos
archivo_proteina=leer_secuencia("proteina")
archivo_adn=leer_secuencia("adn")

#No regresa nada por que no es multiplo de 3
test=traducir(archivo_adn)
#Del website se dice que la cadena empieza desde el caracter 21 hasta 939, pero en python sería 20 y 938 por que inicia en 0.
test2=traducir(archivo_adn[20:938])
print(test2)
print("--------------------------")
#No se incluye por defecto el "_", luego:
test3=traducir(archivo_adn[20:935])
print(test3)
print("--------------------------")
#comprobamos que las cadena sea igual a la traduccion que ofrece la pagina web:
print(archivo_proteina==test3) #Retorna True, luego esta correcto.
print("--------------------------")
#o también podemos cortar el ultimo caracter como en test2, pero del resultado final
test2=traducir(archivo_adn[20:938])[:-1] 
print(archivo_proteina==test2)

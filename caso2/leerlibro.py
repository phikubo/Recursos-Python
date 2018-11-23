print("Lectura de libros")
from diccionario_de_palabras import contar_palabras

def abrir_libro(libro_direccion):
	"""
	Abre el archivo de un libro en .txt y lo regresa como una cadena de texto
	"""
	with open(libro_direccion,"r", encoding="utf8") as cadena_libro:
		texto=cadena_libro.read()
		texto=texto.replace("\n","").replace("\r","")
	return texto

def palabras_estadisticas(palabras_cuentas):
	"""
	Regresa el numero unico de palabras y frecuencia de palabras
	"""
	#in: un diccionario
	#Cuantas palabras hay en el diccionario:
	numero_unico=len(palabras_cuentas)
	#Se obtiene solo los valores o claves de valor del diccionario:
	cuentas= palabras_cuentas.values()
	return(numero_unico, cuentas)

#------------main--------------
#abrimos el archivo y se guarda en lib
lib=abrir_libro("romeo_julieta.txt")
print(len(lib))
#Se busca la cadena de texto en el archivo, regresa el index donde inicia esa cadena.
encontrar=lib.find("What’s in a name?")

print(encontrar, type(encontrar))
print(lib[encontrar:encontrar+100], "...")

#implementamos palabras_estadisticas usando el modulo externo
(unico,cuenta) =palabras_estadisticas(contar_palabras(lib))
#Si se imprime cuenta, se imprime toda la lista de los valores
print(unico,sum(cuenta))



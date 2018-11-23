print("Lectura de libros")


def abrir_libro(libro_direccion):
	"""
	Abre el archivo de un libro en .txt y lo regresa como una cadena de texto
	"""
	with open(libro_direccion,"r", encoding="utf8") as cadena_libro:
		texto=cadena_libro.read()
		texto=texto.replace("\n","").replace("\r","")
	return texto

lib=abrir_libro("romeo_julieta.txt")
print(len(lib))
encontrar=lib.find("What’s in a name?")
print(encontrar, type(encontrar))
print(lib[encontrar:encontrar+100], "...")


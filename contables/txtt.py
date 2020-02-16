
#


def guardar_listas(nombre,data):
	nombre=nombre+".txt"
	with open(nombre, "w") as write_file:
		for i in data:
			write_file.write(str(i))
			write_file.write("\n")
		write_file.close()

if __name__=="__main__":
	pass
else:
	print("guardar lista, ok")

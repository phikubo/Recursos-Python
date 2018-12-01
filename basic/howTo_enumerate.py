print("how to use enumerate")

estaciones= ["primavera", "verano", "otoño", "invierno"]
print(enumerate(estaciones))

print(list(enumerate(estaciones)))

for index, estaciones in enumerate(estaciones):
	print("indice: ", index, ", estaciones: ",estaciones)

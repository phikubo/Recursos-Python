#Visualizador de json
#http://jsonviewer.stack.hu/

import json

print("--------------------------------")
print("Inicio")
print("")

#Diccionario
data = {"Fruteria": [  {"Fruta":   [    {"Nombre":"Manzana","Cantidad":10},    {"Nombre":"Pera","Cantidad":20},    {"Nombre":"Naranja","Cantidad":30}   ]  },  {"Verdura":   [    {"Nombre":"Lechuga","Cantidad":80},    {"Nombre":"Tomate","Cantidad":15},    {"Nombre":"Pepino","Cantidad":50}   ]  } ], "Otra Variable":1}

#string
jdata=json.dumps(data)

#
print("Tipo de variable: ", type(data), " Adentro: ", data["Fruteria"][1]["Verdura"][0]["Cantidad"])
print("--------------------------------")
print("Adentro del diccionario: ", data["Fruteria"][0])
print("Adentro del diccionario: ", data["Fruteria"][1])
print("--------------------------------")
print("Adentro del fruta,0 ", data["Fruteria"][0]['Fruta'][0])
print("Adentro del fruta, 1 ", data["Fruteria"][0]['Fruta'][1])
print("Adentro del fruta, 2 ", data["Fruteria"][0]['Fruta'][2])
print("Adentro del fruta, en cantidad ", data["Fruteria"][0]['Fruta'][0]['Cantidad'])



'''
#json.loads(jdata) #saca el diccionario
print(type(data),type(jdata))

#Guardar el archivo formato json
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

#Lectura de archivo json
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)

'''
print("")
print("--------------------------------")
print("fin")

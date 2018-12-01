#Visualizador de json
#http://jsonviewer.stack.hu/

import json

print("--------------------------------")
print("Inicio")
print("")



#Lectura de archivo json
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    print(data)

#El [0] retira los [] de [{},{},{}], para luego acceder a los {} de adentro.
print("--------------------------------")
print(data['images'])
print("--------------------------------")
print(data['images'][0]['classifiers'][0]['classes'][0])
print("--------------------------------")
print("Clase: ",data['images'][0]['classifiers'][0]['classes'][0]['class'])
print("Porcentaje: ",data['images'][0]['classifiers'][0]['classes'][0]['score'])

print("")
print("--------------------------------")
print("fin")

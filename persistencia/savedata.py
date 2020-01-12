import numpy as np


def nombre_extension(extension):
    """Resuelve el nombre por defecto de un archivo con la extensión deseada"""
    ext="data_"+str(extension)+"."+str(extension)
    return ext


def guardar_data_simple(bandera,ext):
    """Guarda un array simple en un archivo de extensión deseada"""
    data = np.linspace(0,1,201)
    if bandera:
        nombre_archivo_data=nombre_extension(ext)
        np.savetxt(nombre_archivo_data, data)

def guardar_data_lines(bandera,ext):
    """Guarda dos arrays de 2x201 o 201x2"""
    x = np.linspace(0, 200, 201)
    y = np.random.random(201)
    print(np.shape([x, y]))
    print(np.shape(np.transpose([x,y])))
    if bandera:
        nombre_archivo_data=nombre_extension(ext)
        #np.savetxt(nombre_archivo_data, [x, y]) # en dos filas
        #np.savetxt(nombre_archivo_data, np.transpose([x, y])) #en dos columnas
        np.savetxt(nombre_archivo_data, np.column_stack((x,y))) #exactamente igual a transpose


if __name__=="__main__":
	#Prototipo:
    #guardar_data_simple(False,"txt")
    guardar_data_lines(True,"txt")

else:
    print("Importado")


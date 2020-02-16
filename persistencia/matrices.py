# import
import numpy as np


def nombre_extension(extension, complemento):
    """Resuelve el nombre por defecto de un archivo con la extensión deseada"""
    ext = "data_"+str(extension)+"_"+str(complemento)+"."+str(extension)
    return ext

def guardar_with_numpy(data, nombre_archivo, header):
    with open(nombre_archivo, 'wb') as archivo: #si es a+ se hace append
        np.savetxt(archivo, [], header=header)
        np.savetxt(archivo, data, fmt='%4.4f')
        archivo.flush()
        # for i in range(len(data)):
        #data=np.column_stack([x[i], y[i]])
        #np.savetxt(archivo, data,fmt='%4.1f')
        # archivo.flush()
        # time.sleep(0.1)

def cargar_datos(nombre):
    #data=np.loadtxt('data_txt.txt')
    data=np.loadtxt(nombre)
    #x=data[:,0]
    #y=data[:,1]
    return data

def test_persistencia():
    print("alles gut")
    header = "coolumna x, columna y"
    nombre_archivo = nombre_extension("txt", "ncolumnas")
    nombre_archivo2 = nombre_extension("txt", "ncolumnas2")

    x1 = np.linspace(0, 10, 11)
    x2 = np.linspace(11, 21, 11)
    x3 = np.linspace(21, 31, 11)
    x4 = np.linspace(31, 41, 11)
    test = x1.transpose()
    data=np.column_stack((x1,x2))
    data=np.column_stack((data,x3))
    data=np.column_stack((data,x4))
    print(data)
    print(np.shape(data))
    print(data[0])
    #esto muestra que el stack se hace horizontal respecto al eje x
    #pero si
    print("[:,0]", data[:,0]) #consigue el primer array
    data2=data.transpose()
    print(data2)
    print(np.shape(data2))
    print("[0]",data2[0])
    print("breakdown------")
    #guardar_with_numpy(data, nombre_archivo, header)
    #guardar_with_numpy(data2, nombre_archivo2, header)
    var1=cargar_datos('data_txt_ncolumnas.txt') 
    var2=cargar_datos('data_txt_ncolumnas2.txt')
    print(var1)
    print(np.shape(var1))
    print("[0]",var1[0])
    #esto muestra que el stack se hace horizontal respecto al eje x
    #pero si
    print("[:,0]",var1[:,0]) #consigue el primer array
    var2=var1.transpose()
    print(var2)
    print(np.shape(var2))
    print("[0]", var2[0])
    print("[:,0]",var2[:,0]) #consigue el primer array



if __name__ == "__main__":
    # Prototipo:
    test_persistencia()
else:
    print("Modulo <escribir_nombre> importado")

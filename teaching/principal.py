import mod2
import mod1

def funcion():
    mod2.funcion()
    mod1.funcion()

def extraerdatos(tipo):
    tipo=int(tipo)
    if tipo==1:
        print("tipo: ", tipo)
        variable=mod1.datos()
        print(variable)
    elif tipo==2:
        print("tipo: ", tipo)
        variable=mod2.datos()
        print(variable)



if __name__ == "__main__":
    funcion()
    tipo=input("Escriba el tipo de onda: \n")
    extraerdatos(tipo)

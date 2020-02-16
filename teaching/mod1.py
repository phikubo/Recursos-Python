

def funcion():
    print("mod1.py desde funcion")

def datos():
    lista = [1,2,3,4,5,6,7,8,9,10]
    return lista

if __name__ == "__main__":
    print("mod1 ejecutado desde el mismo archivo")
    funcion()
else:
    print("modulo mod1 importado")
    
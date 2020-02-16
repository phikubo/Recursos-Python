print("inicio del programa")
'''
for i in range(10):
    for j in range(10):
        number=7*i+7*j
        if number ==105:
            print("opc1: ",i,j)
        elif number==98:
            print("opc2:",i,j)
        #print(number, "i: ",i , "j:",j)
        '''
contador=0
import time
for i in range(100,200):
    
    number=i/3.0
    f=number-int(number)
    print(number,i)
    if f ==0:
        
        time.sleep(2)
        #contador=contador+1
        #print("es cero")
        g=i/2.0
        par=g-int(g)
        print("g:",g)
        if par == 0:
            #contador=contador+1
            print("par",contador)
        else:
            print(i, "es un numero impar")
            contador=contador+1
    else:
        #print("no es cero")
        pass
    print(contador)
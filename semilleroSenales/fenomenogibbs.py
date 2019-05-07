#Implemtenado por Michael
import numpy as np
import matplotlib.pyplot as plt
import math
import time
#ecuacion de fourier para generar un pulso rectangular con la ecuacion del fenomeno de gibbs    

'''
y(t)=(4/pi)*sum((sen(2*k-1)/(2*k-1))*t), k=1->n
Fuente:http://sistemyse.blogspot.com/

'''


def main(K, N=100):
    y_sum=0
    y_record=[]
    t = np.linspace(0.0, 10.0, N, endpoint=False)
    for k in range(1,K+1):
        ##print(k)
        y = (4/math.pi)*(np.sin((2*k-1)*t)/(2*k-1))
        #y_sum=y #si se puede hacer
        y_sum=np.add(y_sum,y)
        #print(np.shape(y))
        #y_record.append(y)
        plt.plot(t, y_sum)
        #if k>1:
        #    y_sum=np.add(y_record)
        #    plt.plot(t, y_sum)
    plt.plot(t, y_sum)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title('Fenomeno de Gibbs', fontsize=16, color='r')
    plt.grid(True)
    plt.show()
    print("main")





if __name__ == "__main__":
    k=4
    main(k)
else:
    print("importado gibss")
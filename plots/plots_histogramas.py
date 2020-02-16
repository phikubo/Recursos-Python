import numpy as np
import matplotlib.pyplot as plt
print("holi")
print("inicio del programa")
import time

'''definicion para cerrar la venta en un t especifico'''

def close_ventana():
    plt.close()

fig = plt.figure()
timer = fig.canvas.new_timer(interval = 3000) #creating a timer object and setting an interval of 3000 milliseconds
timer.add_callback(close_ventana)

#creamos el vector de la distribucion normal
x=np.random.normal(size=1000)
#llamamos la funcion histograma para plotear, normed ->deprecated
plt.hist(x, density=True, bins=np.linspace(-5,5,21))# 21 es por que siempre se necesita para cada barra dos puntos, al final, n+1, n=barras

y=np.random.gamma(2,3, 10000)
plt.figure()
plt.subplot(221)
plt.hist(y,bins=30)
plt.subplot(222)
plt.hist(y,bins=30, density=True)
plt.subplot(223)
plt.hist(y,bins=30, cumulative=30)
plt.subplot(224)
plt.hist(y,bins=30, density=True, cumulative=True, histtype="step")




plt.grid(True)
timer.start()
plt.show()



































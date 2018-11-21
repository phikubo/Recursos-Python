import numpy as np
import matplotlib.pyplot as plt
print("holi")
print("inicio del programa")
import time
'''FUNCIONES LOGARITMICAS
semilogx()
semilogy()
loglog()
'''


'''definicion para cerrar la venta en un t especifico'''

def close_ventana():
    plt.close()

fig = plt.figure()
timer = fig.canvas.new_timer(interval = 3000) #creating a timer object and setting an interval of 3000 milliseconds
timer.add_callback(close_ventana)


#ejemplo 5, custom plots with logs
''' legend(), axis(), xlabel(), ylabel() y savefig()'''

#es una opcion, la otra es logaritmicamente espaciada
#x=np.linspace(0,10,20)
x=np.logspace(-1,1,40) #0.1, 10, 40
y1=x**2.0
y2= x**1.5
'''
con las dos plots seguidas, las imprime ambas
'''
plt.loglog(x,y1, "bo-", linewidth=2, markersize=12, label='$\sum_{i=0}^\infty x_i$') 
plt.loglog(x,y2, "gs-", linewidth=2, markersize=12, label="second verde")
'''Ajusto los ejes con
	 plt.axis([xmin, xmax, ymin, ymax]) '''


'''Puedo usar latex adentro!!! :D'''
plt.xlabel(r"$\frac{x}{y}$")
plt.ylabel("$y$")
plt.title(r'$\alpha > \beta$', fontsize=16, color='r')
'''mostramos lo que hay en label, con loc="parametro" le decimos donde queremos que este las 
lineas de cada funcion y1 o y2 correspondientes'''
plt.legend(loc="upper left") 


#ejepmlo 2
#x=np.logspace(0,1,10)
#y=x**2
#plt.loglog(x,y,"bo-") 




plt.grid(True)
plt.savefig("miprimeraimagen.pdf")
timer.start()
plt.show()



































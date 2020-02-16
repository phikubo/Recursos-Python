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


#ejample 1
#plt.plot([0,1,5,7,8, 0])

#ejemplo 2
#x=np.linspace(0,10,20)
#y=x**2.0
#plt.plot(x,y)

#ejemplo 3

#x=np.linspace(0,10,20)
#y1= x**2.0
#y2= x**1.5
##plt.plot(x,y1, "bo-") #bo-: b-blue, o-circles, - lines
#plt.plot(x,y2, "gs-", linewidth=2, markersize=12)

#ejemplo 4
#plt.plot([0,1,2],[0,1,4],"rd-") 

#ejemplo 5, custom plots
''' legend(), axis(), xlabel(), ylabel() y savefig()'''

x=np.linspace(0,10,20)
y1=x**2.0
y2= x**1.5
'''
con las dos plots seguidas, las imprime ambas
'''
plt.plot(x,y1, "bo-", linewidth=2, markersize=12, label='$\sum_{i=0}^\infty x_i$') 
plt.plot(x,y2, "gs-", linewidth=2, markersize=12, label="second verde")
'''Ajusto los ejes con
	 plt.axis([xmin, xmax, ymin, ymax]) '''

plt.axis([-1, 5, -1.5, 6])
'''Puedo usar latex adentro!!! :D'''
plt.xlabel(r"$\frac{x}{y}$")
plt.ylabel("$y$")
plt.title(r'$\alpha > \beta$', fontsize=16, color='r')
'''mostramos lo que hay en label, con loc="parametro" le decimos donde queremos que este las 
lineas de cada funcion y1 o y2 correspondientes'''
plt.legend(loc="upper left") 






plt.grid(True)
plt.savefig("miprimeraimagen.pdf")
timer.start()
plt.show()



































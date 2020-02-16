import numpy as np
import matplotlib.pyplot as plt
import time
import random
print("inicio del programa")

#ejemplo1
tiempo_inicio=time.clock()
rolls4=np.random.randint(1,7,(10000000,10))
sumrolls=np.sum(rolls4, axis=1)
tiempo_final=time.clock()
print("tiempo transcurrido hata el final del calculo: ",tiempo_final-tiempo_inicio)
#plt.show()
















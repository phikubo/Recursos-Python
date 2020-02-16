import numpy as np
import matplotlib.pyplot as plt
import time
import random
print("inicio del programa")

#ejemplo1
X0=np.array([[0],[0]])
#print(X0)
delta_x=np.random.normal(0,1, (2,10000))
#print(delta_x, "comulativa: ", np.cumsum(delta_x,axis=1))
X=np.concatenate((X0, np.cumsum(delta_x,axis=1)),axis=1)
plt.plot(delta_x[0], delta_x[1], "go-") #x=fila 0, y=fila 1
plt.plot(X[0], X[1], "bo-") #x=fila 0, y=fila 1
#plt.savefig("mifig.pdf")
plt.show()
















#Implementado por Michael

from scipy import signal
from scipy.fftpack import fft
import numpy as np
import matplotlib.pyplot as plt

N=600 #para este ejercicio debe ser par

def calculadorafft(T, N=600):
    t = np.linspace(0.0, 1.0, N, endpoint=False)
    sig=signal.square(2*np.pi*5*t, duty=T)
    fftsig=fft(sig)
    plt.subplot(211)
    plt.grid(True)
    #como calcular envolvente del dominio de la frec?
    plt.plot(t,T*np.sinc((T/2)*(5*t))[0:N])
    plt.plot(t, (2.0/N)*np.abs(fftsig[0:int(N)]))
    plt.subplot(212)
    plt.plot(t,sig[0:int(N)])
    #plt.savefig("fftsignal"+str(T)+".png")
    plt.grid(True)
    plt.show()

def calculadorafft_3f(T, N=600):
    t = np.linspace(0.0, 1.0, N, endpoint=False)
    sig=signal.square(2*np.pi*5*t, duty=T)
    
    fftsig=fft(sig)
    plt.subplot(311)
    plt.plot(t, 2.0/N*np.abs(fftsig[0:int(N)]))
    plt.subplot(312)
    plt.plot(t[1:], 2.0/N*np.abs(fftsig[0:int(N)])[1:])
    plt.subplot(313)
    plt.plot(t,sig[0:int(N)])
    plt.savefig("fftsignal"+str(T)+".png")
    plt.show()

def calculadorafft_xf(T, N=600):
    t = np.linspace(0.0, 1.0, N, endpoint=False)
    sig=signal.square(2*np.pi*5*t, duty=T)
    xf=np.linspace(0.0, 1.0/(2.0*T), N/2)
    fftsig=fft(sig)
    plt.subplot(311)
    plt.plot(xf, 2.0/N*np.abs(fftsig[0:int(N/2)]))
    plt.subplot(312)
    plt.plot(xf[1:], 2.0/N*np.abs(fftsig[0:int(N/2)])[1:])
    plt.subplot(313)
    plt.plot(xf,sig[0:int(N/2)])
    plt.savefig("fftsignal"+str(T)+".png")
    plt.show()
#x
lista=[1/10, 2/10, 3/10, 4/10, 5/10, 9/10]
print(lista)

for i in lista:
    calculadorafft(i)
'''
t = np.linspace(0.0, 1.0, N, endpoint=False)
print(len(t))
#y
sig=signal.square(2*np.pi*5*t, duty=T)
####the definition of xf maps the fft bins to frequencies
xf=np.linspace(0.0, 1.0/(2.0*T), N/2)
print(len(xf))
fftsig=fft(sig)
#plot(x,y)
#plt.plot(fftsig)
plt.subplot(311)
plt.plot(xf, 2.0/N*np.abs(fftsig[0:int(N/2)]))
plt.subplot(312)
plt.plot(xf[1:], 2.0/N*np.abs(fftsig[0:int(N/2)])[1:])
plt.subplot(313)
plt.plot(xf,sig[0:int(N/2)])
#plt.plot(t, sig)
plt.ylim(-2, 2)
plt.show()
'''

import numpy as np
import math
import random
import time


def horn(tilt):
	'''Modela el tipo de antena TS 36.942'''
	theta = np.linspace(-np.pi, np.pi, 200)
	theta2= np.linspace(-180,180, 180)
	print(len(theta), len(theta2))
	print(theta2)


if __name__=="__main__":
	horn(10)
else:
	print("Modulo Antena importado")

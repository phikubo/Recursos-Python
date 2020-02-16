import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = plt.axes()
patch = mpatches.Circle((325, 245), 180, alpha=0.5, transform=None)
fig.artists.append(patch)


plt.show()

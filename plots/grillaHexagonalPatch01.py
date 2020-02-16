import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np
<<<<<<< HEAD
#http://magomar.github.io/deludobellico//programming/java/hexagonal-maps/2013/10/10/mapas-hexagonales-2.html
#https://joseguerreroa.wordpress.com/2016/11/17/como-producir-rejillas-grid-hexagonales-mediante-pyqgis/
#https://gamedevelopment.tutsplus.com/es/tutorials/introduction-to-axial-coordinates-for-hexagonal-tile-based-games--cms-28820
#https://gamedevelopment.tutsplus.com/es/tutorials/hexagonal-character-movement-using-axial-coordinates--cms-29035

#coord_0 = [[0,0,0],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1],[1,-1,0],[1,0,-1]]
coord = [[0,0,0],[0,3,-3],[-3,3,0],[-3,0,3],[0,-3,3],[3,-3,0],[3,0,-3]]
#cuales serían las coordenadas para una grilla mas grande. Existe algun algoritmo para sacar las 
#coordenadas de forma dinamica?. Que cada hexagono se ubique del centro hacia afuera y cada suma
#se ubique contra las manecillas del reloj.
colors = [["Green"],["Blue"],["Green"],["Green"],["Red"],["Green"],["Green"]]
labels = [['0,0,0'],['0,3,-3'],['-3,3,0'],['-3,0,3'],['0,-3,3'],['3,-3,0'],['3,0,-3']]
#orden = [ [],[],[],[],[],[],[] ]
=======

coord = [[0,0,0],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1],[1,-1,0],[1,0,-1]]
colors = [["Green"],["Blue"],["Green"],["Green"],["Red"],["Green"],["Green"]]
labels = [['yes'],['no'],['yes'],['no'],['yes'],['no'],['no']]

>>>>>>> e72d06c33da3409d3341ff2f016d5721a272f90e
# Horizontal cartesian coords
hcoord = [c[0] for c in coord]

# Vertical cartersian coords
vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]

fig, ax = plt.subplots(1)
ax.set_aspect('equal')

# Add some coloured hexagons
for x, y, c, l in zip(hcoord, vcoord, colors, labels):
    color = c[0].lower()  # matplotlib understands lower case words for colours
<<<<<<< HEAD
    hex = RegularPolygon((x, y), numVertices=6, radius=2, 
                         orientation=np.radians(30), #con 60 grados funciona perfecto, pero las coordenadas cambian. Antes 30
                         facecolor=color, alpha=0.2, edgecolor='k')
                         #cambiar radius=2. / 3. , cuando se usa coord_0
=======
    hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3., 
                         orientation=np.radians(30), 
                         facecolor=color, alpha=0.2, edgecolor='k')
>>>>>>> e72d06c33da3409d3341ff2f016d5721a272f90e
    ax.add_patch(hex)
    # Also add a text label
    ax.text(x, y+0.2, l[0], ha='center', va='center', size=20)

# Also add scatter points in hexagon centres
ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)
plt.grid(True)
plt.show()

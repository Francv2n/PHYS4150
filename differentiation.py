#5.21: Electric field of a charge distribution
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
def Potential(q, r0, x, y, k=1):
    den = np.hypot(x-r0[0], y-r0[1])
    return k*q/(den+0.001)
nx, ny = 100, 100 
x = np.linspace(-50, 50, nx)
y = np.linspace(-50, 50, ny)
X, Y = np.meshgrid(x, y)
charges = [(-1,(5,0)), (1,(-5,0))]
V = np.zeros((ny, nx))
for charge in charges: 
    ev = Potential(*charge, x=X, y=Y)
    V += ev
fig = plt.figure(figsize=(7,7)) 
plt.contourf(X, Y, V, 20, cmap='RdGy')
plt.colorbar()
Ey, Ex = np.gradient(V, x, y) 
fig = plt.figure(figsize=(8,8)) 
ax = fig.add_subplot(111)
color = np.log(np.hypot(Ex, Ey)) 
ax.streamplot(X, Y, Ex, Ey, color = color, linewidth=1, cmap=plt.cm.inferno,
              density=1, arrowstyle='->', arrowsize=1.5)
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in charges: # plotting the charge points.
    ax.add_artist(Circle(pos, 1, color=charge_colors[q>0]))

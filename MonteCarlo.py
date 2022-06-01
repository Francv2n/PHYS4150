#Exercise 10.3: Brownian motion
import numpy as np
import matplotlib.pyplot as plt
def brownian_motion(L, N):
   # initialize position in the center of the grid
   x = L // 2
   y = L // 2
   # initialize the grid
   grid = np.zeros((L, L), dtype=np.int32)
   # loop over the number of steps
   for i in range(N):
       # choose a random direction
       direction = np.random.choice(['up', 'down', 'left', 'right'])
       # move one step in that direction
       if direction == 'up':
           y += 1
       elif direction == 'down':
           y -= 1
       elif direction == 'left':
           x -= 1
       elif direction == 'right':
           x += 1
       # make sure the particle is still on the grid
       if x < 0 or x >= L or y < 0 or y >= L:
           continue
       # update the grid
       grid[y, x] = 1
   return grid
if __name__ == '__main__':
   # set the size of the grid
   L = 101
   # set the number of steps
   N = 1000000
   # generate the grid
   grid = brownian_motion(L, N)
   # plot the grid
   plt.imshow(grid, cmap='binary')
   plt.show()
#Exercise 10.8: Calculate a value for the integral
from pylab import *
N = 10000000
z = random(N)
x = z**2
def g(x):
	return 1/(1+exp(x))
I = sum(g(x))/N*2
print('I = {}'.format(I))

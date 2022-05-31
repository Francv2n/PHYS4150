#Exercise 10.3: Brownian motion
#Exercise 10.8: Calculate a value for the integral
from pylab import *
N = 10000000
z = random(N)
x = z**2
def g(x):
	return 1/(1+exp(x))
I = sum(g(x))/N*2
print('I = {}'.format(I))

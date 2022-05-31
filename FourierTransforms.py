from numpy import exp, arange, pi, zeros,linspace, ones
from pylab import *
def dft(y):
	N = len(y)
	c = zeros(N//2 +1,complex)
	n = arange(0,N)
	for k in range(N//2 + 1):
		c[k] = sum(y*exp(-1j*2*pi*k*n/N))
	return c
N = 1000
y1 = ones(N)
y1[:N//2]=0
plot(y1)
show()
c1 = dft(y1)
plot(abs(c1[100:200]))
show()
y2 = arange(N)
c2 = dft(y2)
plot(abs(c2))
show()
n = arange(N)
y3 = sin(pi*n/N)*sin(20*pi*n/N)
plot(y3)
show()
c3 = dft(y3)
plot(abs(c3))
show()

#exercise 9.8
!pip install vpython
import cmath
from pylab import *
from numpy import copy
from vpython import *
def banded(Aa,va,up,down):
    # Copy the inputs and determine the size of the system
    A = copy(Aa)
    v = copy(va)
    N = len(v)
    # Gaussian elimination
    for m in range(N):
        # Normalization factor
        div = A[up,m]
        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]
        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]
    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]
    return v
h = 1e-18*10
hbar = 1.0546e-36
L = 1e-8
M = 9.109e-31
N = 1000 # Grid slices
a = L/N
a1 = 1 + h*hbar/2/M/a**2*1j
a2 = -h*hbar*1j/4/M/a**2
b1 =  1 - h*hbar/2/M/a**2*1j
b2 =  h*hbar*1j/4/M/a**2
ksi = zeros(N+1,complex)
def ksi0(x):
  x0 = L/2
  sigma = 1e-10
  k = 5e10
  return_this = []
  for val in x:
    new = exp(-(val-x0)**2/2/sigma**2)*(np.exp(1j*k*val))
    return_this.append(new)
  return np.asarray(return_this)
x = linspace(0,L,N+1)
ksi[:] = ksi0(x)
ksi[[0,N]]=0
A = empty((3,N),complex)
A[0,:] = a2
A[1,:] = a1
A[2:,] = a2
from vpython import curve, rate
ksi_c = curve()
ksi_c.set_x(x-L/2)
#ksi = banded(A,v,1,1)
while True:
	rate(39)
	ksi_c.set_y(real(ksi)*1e-9)
	ksi_c.set_z(imag(ksi)*1e-9)	
	for i in range(20):
		v = b1*ksi[1:N] + b2*(ksi[2:N+1] + ksi[0:N-1])
		ksi[1:N] = banded(A,v,1,1)
#exercise 9.9
!pip install vpython 
from pylab import *
from numpy import copy
from vpython import *
def banded(Aa,va,up,down):
    # Copy the inputs and determine the size of the system
    A = copy(Aa)
    v = copy(va)
    N = len(v)
    # Gaussian elimination
    for m in range(N):
        # Normalization factor
        div = A[up,m]
        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]
        # Now normalize the pivot row of A and subtract from lower ones
        for i in range(up):
            j = m + up - i
            if j<N:
                A[i,j] /= div
                for k in range(1,down+1):
                    A[i+k,j] -= A[up+k,m]*A[i,j]
    # Backsubstitution
    for m in range(N-2,-1,-1):
        for i in range(up):
            j = m + up - i
            if j<N:
                v[m] -= A[i,j]*v[j]
    return v
h = 2e-18*10
hbar = 1.0546e-36
L = 1e-8
M = 9.109e-31
N = 1000 # Grid slices
a = L/N
def complex_arg(trans):	
	def f(y):
		return trans(real(y)) + 1j*trans(imag(y))
	return f
@complex_arg
def dst(y):
    N = len(y)
    y2 = empty(2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -imag(rfft(y2))[:N]
    a[0] = 0.0
    return a
@complex_arg
def idst(a):
    N = len(a)
    c = empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = irfft(c)[:N]
    y[0] = 0.0
    return y
ksi = zeros(N+1,complex)
def ksi0(x):
	x0 = L/2
	sigma = 1e-10
	k = 5e10
	return exp(-(x-x0)**2/2/sigma**2)*exp(1j*k*x)
x = linspace(0,L,N+1)
ksi[:] = ksi0(x)
ksi[[0,N]]=0
b0 = dst(ksi)
t = 1e-18
b_ = b0*exp(1j*pi**2*hbar*arange(1,N+2)**2/2/M/L**2*t)
ksi_ = idst(b_)
plot(ksi_)
show()
from vpython import curve, rate
ksi_c = curve()
ksi_c.set_x(x-L/2)
#ksi = banded(A,v,1,1)
t = 0
while True:
	rate(30)
	b_ = b0*exp(1j*pi**2*hbar*arange(1,N+2)**2/2/M/L**2*t)
	ksi_ = idst(b_)
	ksi_c.set_y(real(ksi_)*1e-9)
	ksi_c.set_z(imag(ksi_)*1e-9)
	t +=h*5

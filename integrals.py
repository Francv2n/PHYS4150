#Exercise 5.12: The Stefan–Boltzmann constant
from math import *
import numpy as np
from scipy import integrate
integration = lambda x: (x**3)/((np.exp(x))-1)
y,err = integrate.quad(integration, 0, np.inf)
y
boltz=1.380649*10**(-23)
pi=3.14
c=2.99792*10**8
hbar=1.054571*10**(-34)
a=(boltz**4*y)/(4*pi**2*c**2*hbar**3)
print "The Stefan-Boltzmann constant is=",a

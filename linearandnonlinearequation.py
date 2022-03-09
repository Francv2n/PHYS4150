#1
import numpy as np 
import matplotlib.pyplot as plt
w =1
V =20
val = np.sqrt(9.10938356e-31*1.60217662e-19)*1e-9/(np.sqrt(2)*1.05457180013e-34)
E = np.linspace(0.0, V, 100000)
num = int(round((w*np.sqrt(V)*val-np.pi/2.0)/np.pi))
for n in range(100000):
    for m in range(num+2):
        if abs(E[n]-((2.0*float(m)+1.0)*np.pi/(2.0*w*val))**2)<0.01: E[n] = np.nan
        if abs(E[n]-(float(m)*np.pi/(w*val))**2)<0.01: E[n] = np.nan
y1 = np.tan(np.sqrt(E)*val)
y2 = np.sqrt((V-E)/E)
y3 = -np.sqrt(E/(V-E))
plt.plot(E,y1,label="y1")
plt.plot(E,y2,label="y2")
plt.plot(E,y3,label="y3")
plt.xticks(range(0,25,5))
plt.ylim(-8,8)
plt.show()
#2
print ("The values of first six energy levels are:")
f_even = lambda E : np.sqrt(V-E)-np.sqrt(E)*np.tan(w*np.sqrt(E)*val)
f_odd = lambda E : np.sqrt(V-E)+np.sqrt(E)/np.tan(w*np.sqrt(E)*val)
E_old = 0.0
f_even_old = f_even(0.0)
f_odd_old = f_odd(0.0)
n = 0
E_vals = np.zeros(999)
for E in np.linspace(0.0, V, 200000):
    f_even_now = f_even(E)
    if f_even_now == 0.0 or f_even_now/f_even_old < 0.0:
        if (abs(f_even_now)<1.0 and abs(f_even_old)<1.0):
            E_vals[n-1] = (E+E_old)/2.0
            print( "  State #%3d (Even wavefunction): %9.4f eV,"%(n,E_vals[n-1]))
            n += 1
    f_odd_now = f_odd(E)
    if f_odd_now == 0.0 or f_odd_now/f_odd_old < 0.0:
        if (abs(f_odd_now)<1.0 and abs(f_odd_old)<1.0):
            E_vals[n-1] = (E+E_old)/2.0
            print( "  State #%3d  (Odd wavefunction): %9.4f eV,"%(n,E_vals[n-1]))
            n += 1
    E_old = E
    f_even_old = f_even_now
    f_odd_old = f_odd_now
    if n>6:
      break

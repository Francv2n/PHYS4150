#exercise 3.2 1
import numpy as np
import matplotlib.pyplot as plt
import math
theta1 = np.linspace(0,2*np.pi,100)
x = 2*np.cos(theta1) + np.cos(2*theta1)
y = 2*np.sin(theta1) - np.sin(2*theta1)
plt.plot(x,y)
plt.xlabel('x axis')
plt.title('Deltoid Curve')
plt.ylabel('y axis')
plt.show()

#2
import numpy as np
import matplotlib.pyplot as plt
theta1 = np.linspace(0,10*np.pi,100)
r = theta1**2
x = r*np.cos(theta1)
y = r*np.sin(theta1)
plt.plot(x,y)
plt.xlabel('x axis')
plt.title('Polar Curve')
plt.ylabel('y axis')
plt.show()

#3
import numpy as np
import matplotlib.pyplot as plt
theta1 = np.linspace(0,24*np.pi,5000)
r = np.exp(np.cos(theta1)) - 2*np.cos(4*theta1) + np.sin(theta1/12)**5
x = r*np.cos(theta1)
y = r*np.sin(theta1)
plt.plot(x,y)
plt.xlabel('x axis')
plt.title('Fey''s Function')
plt.ylabel('y axis')
plt.show()

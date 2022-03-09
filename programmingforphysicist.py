#another ball from a tower
import math
h = float(input("Enter the height: "))
t = math.sqrt(2*h/9.8)
t = float("{0:.3f}".format(t))
print("Time taken is: ",t)
#exercise 2.4
import math
v = float(input("Enter Relative Speed (as a fraction of the speed of light c): "))
x = float(input("Enter distance of spaceship from another planet in lightyears: "))
t0 = x / v
print("\nTime in years (In the rest frame of an observer on Earth): {:.2f}".format(t0), "Years")
ts = (t0*(math.sqrt(1 - v**2)))
print("\nTime in years (As perceived by a passenger on board the ship): {:.2f}".format(ts), "Years")

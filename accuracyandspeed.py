#exercise 4.3 : calculating derivatives 
def f(x):
    return x * (x - 1)
delta = [10 ** -2, 10 ** -6, 10 ** -8, 10 ** -10, 10 ** -12, 10 ** -14]
trueValue = 1  # deriative of x^-x=2*x-1,at x=1 it becomes 1
for i in delta:
    term = (f(1 + i) - f(1)) / i
    error = abs(trueValue - term)
    print('For delta={:.2e}'.format(i), ' Deravative calculated={:15.14f}'.format(term), 'Error={:e}'.format(error))
#exercise 4.4 : calculating integrals 
#1.
import math
N = 100
h=2/N
integral_result = 0
for k in range(1,N+1):
    xk = -1 + h*k 
    yk = math.sqrt(1-(xk**2))
 	integral_result += h*yk
print(f"Actual Value: {math.pi*0.5}")
print(f"Result using Riemman integral (N={N}): {integral_result}")
#2. 
import math
from time import time
N = 2840000
h=2/N
integral_result = 0
start_time = time()
for k in range(1,N+1):
    xk = -1 + h*k 
    yk = math.sqrt(1-(xk**2))
    integral_result += h*yk
#Time the end of the loop
end_time = time()
print(f"Time measured: {end_time-start_time} seconds")
print(f"Actual Value: {math.pi*0.5}")
print(f"Result using Riemman integral (N={N}): {integral_result}")

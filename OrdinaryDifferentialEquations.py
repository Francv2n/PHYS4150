#Exercise 8.7: Trajectory with air resistance
from numpy import arange,empty, array
from pylab import *
from cmath import exp
class rksolve:
	def __init__(self,f):
		self.f = f
		self.initial_conditions = None
		self.solution = None
	def iterate(self,a,b,N=1000):
		f = self.f
		r0 = array(self.initial_conditions,float)
		h = (b-a)/N
		tpoints = arange(a,b,h)
		solution = empty(tpoints.shape + r0.shape,float)
		#r_points[0] = r0
		r = r0
		for i,t in enumerate(tpoints):
		    solution[i]=r
		    k1 = h*f(r,t)
		    k2 = h*f(r+0.5*k1,t+0.5*h)
		    k3 = h*f(r+0.5*k2,t+0.5*h)
		    k4 = h*f(r+k3,t+h)
		    r += (k1+2*k2+2*k3+k4)/6
		self.h = h
		self.solution = solution
		self.t = tpoints
def array_decorator(f,*args,**kwargs):	
	print('function decorated to return array')
	g = lambda *args,**kwargs: array(f(*args,**kwargs),float)
	return g
def trajectory(m=1):
	ro = 1.22
	C = 0.47
	g = 9.81
	R = 8e-2	
	@array_decorator
	def f(r,t):
		x,y,vx,vy = r
		v = sqrt(vx**2 + vy**2)
		F_fr = 1/2*pi*R**2*ro*C*v**2
		Dr = [vx,vy]
		Dvx = -F_fr/m*vx/v
		Dvy = -F_fr/m*vy/v - g
		Dv = [Dvx,Dvy]
		return Dr + Dv
	prob = rksolve(f)
	r0 = [0,0]
	v0e = 100*exp(1j*30/180*pi)
	v0 = [v0e.real,v0e.imag]
	prob.initial_conditions = r0 + v0
	prob.iterate(0,10)
	x = prob.solution[:,0]
	y = prob.solution[:,1]
	plot(x[y>0],y[y>0],label=m)
	return x[abs(y)<0.2][-1]
m_range = arange(0.5,5,0.05)
x_ground = [trajectory(m) for m in m_range]
legend()
show()
plot(m_range,x_ground)
xlabel('m')
ylabel('x')
show()
#Exercise 8.4:
!pip install vpython
from math import sin,pi
from numpy import array,arange
from pylab import plot,xlabel,show
from vpython import *
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -g/l*sin(theta)
    return array([ftheta,fomega],float)
g = 9.81
l = 0.1
a = 0.0
b = 10.0
N = 3000
h = (b-a)/N
tpoints = arange(a,b,h)
theta = []
r = array([179/180*pi,0],float)
for t in tpoints:
    theta.append(r[0])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
plot(tpoints,theta)
#plot(tpoints,ypoints)
xlabel("t")
show()
class pendulum_xyz:
	def __init__(self,length):
		self.length = length
		from vpython import sphere, cylinder,box,color
		self.cylinder = cylinder(radius =0.1) 
		#self.cylinder.axis = self.x,self.y,self.z
		self.sphere = sphere(radius=0.5)
		self.sphere.color = color.red
		#self.sphere.pos = self.x,self.y,self.z
		#self.update_pos()
		self.box = box(lenght=2,width=2,height=0.1)
		self.box.pos = 0,0,-0.1/2
		#self.pos = pos
		self.setpos([0,length,0]) 
		#d = display()
	@property
	def getpos(self):
		print('Getting position')
		return self._pos
	def setpos(self,pos):
		pos[1]=-pos[1]
		print('Position set to {}'.format(pos))
		self._pos = pos
		self.cylinder.axis = pos
		self.sphere.pos = pos
	#pos = property(getpos,setpos)
class pendulum_theta(pendulum_xyz):
	from cmath import exp
	#def __init__(self)
	def angle(self,theta):
		r = self.length*exp(1j*theta)
		self.setpos([r.imag,r.real,0])	
p = pendulum_theta(10)
from vpython import rate
for t,angle in zip(tpoints,theta)[::10]:
	rate(240)
	p.angle(angle)

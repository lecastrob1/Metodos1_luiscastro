import numpy as np
import matplotlib.pyplot as plt

B0=0.05
fr=7
omh=3.5
R=1.75
r=25/2
def funcion(B0,fr,omh,r,t):
    flu=2*(np.pi)*fr*t
    rot=omh*t
    return B0*(np.cos(flu))*(np.pi)*(r**2)*(np.cos(rot))
def derivada(f,t,h,B0,fr,omh,r):
    
    d = 0.
    
    if h != 0:
        d = (f(B0,fr,omh,r,t+h) - f(B0,fr,omh,r,t-h))/(2*h)       
    return d

t = np.linspace(0,4*np.pi,10000)
h = t[1] - t[0]
y=-(1/R)*derivada(funcion,t,h,B0,fr,omh,r)
def momentos0(x, y):
    indices = np.where(np.round(y, 0) == 0)[0]
    lis = [x[i] for i in indices]
    if len(lis) > 3:
        lis.sort()
        lis = lis[:3]
       
    return lis
print(momentos0(t,y))
plt.scatter(t,y)
plt.axhline(0, color='red', linestyle='--')
plt.show()



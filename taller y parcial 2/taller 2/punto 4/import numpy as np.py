import numpy as np
import matplotlib.pyplot as plt
#4.1
N = 1000000
a = 0
b = np.pi
x = np.random.uniform(a,b,N)
def func_integrate(x):
    return np.exp(-x)*np.sin(x)
    
fi = func_integrate(x)
I = (b-a)*sum(fi)/N
Iteo = 0.5*(1+np.exp(-np.pi))
error=(np.abs(Iteo-I))/Iteo

def err(N,fi):
    a = 0
    b = np.pi
    Iteo = 0.5*(1+np.exp(-np.pi))
    error=(np.abs(Iteo-((b-a)*sum(fi)/N)))/(((b-a)*sum(fi)/N))
    return error
bas=np.linspace(1, 100, 100)
y=err(bas,fi)
enes=np.linspace(1, 100, 100)
rai=1/((enes)**(1/2))
plt.plot(bas,y,label='datos')
plt.plot(enes,rai,label='1/swrt()')
plt.legend()
plt.show()

#4.2
a=0
b=2*np.pi
N = 1000000
ger = np.random.uniform(a,b,N)

#masa
def fun_flor(x):
    return np.cos(2*x)**3
cir = fun_flor(ger)
totacir = (b-a)*sum(cir)/N

#centro de masa x
def cx(x):
    return np.cos(2*x)**3*np.cos(x)
cirx = cx(ger)
totax = (b-a)*sum(cirx)/N
#centro de masa y
def cy(x):
    return np.cos(2*x)**3*np.sin(x)
ciry = cy(ger)
totay= (b-a)*sum(ciry)/N
print('el centro de masa en x es'+str(totax)+' y en y es '+str(totay) )

def inerci(x):
    return np.cos(2*x)**5
iner = inerci(ger)
totaienr= (b-a)*sum(iner)/N
print(totaienr)
#4.3
R = 1
x = np.random.uniform(-R,R,N)
y = np.random.uniform(-R,R,N)
z=np.random.uniform(-R,R,N)
def f(x, y, z):
    return np.sin(x**2 + y**2 + z**2) * np.exp(x**2 + y**2 + z**2)
suma=f(x, y, z)
asma = (2*R)**3*sum(suma)/N
print(asma)




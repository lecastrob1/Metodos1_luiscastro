import numpy as np
 
def f(x):
    return np.abs(x-2)
Dx = lambda f,x,h=1e-5: (f(x+h) - f(x-h))/(2*h)
_x = np.linspace(-10,10,50)
F = f(_x)
def Minimizer(f, N=1000, gamma=0.01):
    
    r = np.zeros(N)
    # Seed
    r[0] = np.random.uniform(-5,5)
    
    for i in range(1,N):
        r[i] = r[i-1] - gamma*Dx(f,r[i-1])
        
    return r
x = Minimizer(f)
print(x[-1])
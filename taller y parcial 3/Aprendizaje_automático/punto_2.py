import numpy as np

def f2(x,y):
    return x**4 + y**4 - 2*(x-y)**2
    #return 14*x**2 - 2*x**3 + 2*y**2 + 4*x*y
Dx = lambda f,x,y,h=1e-5: (f(x+h,y) - f(x-h,y))/(2*h)
Dy = lambda f,x,y,h=1e-5: (f(x,y+h) - f(x,y-h))/(2*h)
x0, y0 = 0.,3.
Gradient = lambda f,x,y: np.array([Dx(f,x,y),Dy(f,x,y)])
Gradient(f2,x0,y0)
def Minimizer(f, N, gamma = 0.01):
    
    r = np.zeros((N,2))
    r[0] = np.random.uniform(-5.,5.,size=2)
    
    Grad = np.zeros((N,2))
    Grad[0] = Gradient(f,r[0,0],r[0,1])
    
    for i in range(1,N):
        r[i] = r[i-1] - gamma*Gradient(f,r[i-1,0],r[i-1,1])
        Grad[i] = Gradient(f,r[i-1,0],r[i-1,1])
        
        
    return r,Grad
def Minimizer_momentum(f, N, gamma = 0.001, eta=0.6):
    
    r = np.zeros((N,2))
    r[0] = np.random.uniform(-5.,5.,size=2)
    r[1] = np.random.uniform(-5.,5.,size=2)
    r[2] = np.random.uniform(-5.,5.,size=2)
    
    Grad = np.zeros((N,2))
    Grad[0] = Gradient(f,r[0,0],r[0,1])
    i=3
    for i in range(3,N):
        r[i] = r[i-1] - gamma*Gradient(f,r[i-1,0],r[i-1,1])+eta*(r[i-2]-r[i-3])
        Grad[i] = Gradient(f,r[i-1,0],r[i-1,1])
    return r,Grad
N = 900
r,Grad = Minimizer_momentum(f2,N)
r1,grad1=Minimizer(f2,N)
print(r1)
print(r)



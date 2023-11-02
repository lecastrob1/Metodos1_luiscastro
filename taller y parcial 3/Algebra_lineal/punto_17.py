from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
import sympy as sym
import numpy as np

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
def f(x,y):
    
    z = x + sym.I*y
    f = z**3 - 1
    f = f.expand()
    return sym.re(f),sym.im(f)

f0,f1 = f(x,y)
F = [f0,f1]
J = sym.zeros(2,2)

for i in range(2):
    for j in range(2):
        if j==0:
            J[i,j] = sym.diff(F[i],x,1)
        else:
            J[i,j] = sym.diff(F[i],y,1)

InvJ = J.inv(method='LU')

Fn = sym.lambdify([x,y],F,'numpy')
IJn = sym.lambdify([x,y],InvJ,'numpy')

def NewtonRaphson(z,Fn,Jn,itmax=1000000,precision=1e-7):
    
    error = 1
    it = 0
    
    while error > precision and it < itmax:
        
        IFn = Fn(z[0],z[1])
        IJn = Jn(z[0],z[1])
        
        z1 = z - np.dot(IJn,IFn)
        
        error = np.max( np.abs(z1-z) )
        
        z = z1
        it +=1
        
    return z
z0=np.array([0.5,0.5])
zsol = NewtonRaphson(z0,Fn,IJn)
print(zsol)


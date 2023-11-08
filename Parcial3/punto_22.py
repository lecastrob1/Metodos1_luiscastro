from IPython.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))
import matplotlib.pyplot as plt
import sympy as sym
import numpy as np

x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
cu=9*10**9
k=((np.sqrt(2)/2)+(1/4))*(1/114.6)*(3*10**-4)**2*cu*(1/5**2)
def f(x,y):
    
    z = x + sym.I*y
    f = sym.sin(z)**6+k**2*sym.sin(z)**2-k**2
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

InvJ = J.inv()
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


def guardar_lista(lista_grande):
    n=25
    x=np.linspace(-1,1,n)
    y=np.linspace(-1,1,n)
    for i in range(n):
     for j in range(n):
        z0=np.array([x[i],y[j]])
        array=NewtonRaphson(z0, Fn, IJn)
        array=np.around(array,decimals=5)
        if not any(np.array_equal(array, arr) for arr in lista_grande):
         lista_grande.append(array)
    return lista_grande

lista_grande = []
lista_grande = guardar_lista(lista_grande)
print(lista_grande)


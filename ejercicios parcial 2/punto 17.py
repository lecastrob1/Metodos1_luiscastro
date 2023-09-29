import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from sympy import symbols, oo, exp, integrate


x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)

def GetLaguerre(k,x):

    if k==0:
        poly = sym.Number(1)
    elif k==1:
        poly = 1-x
    else:
        poly = ((2*k-1-x)*GetLaguerre(k-1,x)-(k-1)*GetLaguerre(k-2,x))/k
   
    return sym.expand(poly,x)
def GetDLaguerre(n,x):
    Pn = GetLaguerre(n,x)
    return sym.diff(Pn,x,1)
def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots    
def GetAllRootsGLag(n):
    limi=n+(n-1)*np.sqrt(n)

    xn = np.linspace(0,limi,1000)
    
    Legendre = []
    DLegendre = []
    
    for i in range(n+1):
        Legendre.append(GetLaguerre(i,x))
        DLegendre.append(GetDLaguerre(i,x))
    
    poly = sym.lambdify([x],Legendre[n],'numpy')
    Dpoly = sym.lambdify([x],DLegendre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)
    Laguerre = []
    
    for i in range(n+2):
        Laguerre.append(GetLaguerre(i,x))       
    polyla = sym.lambdify([x],Laguerre[n+1],'numpy')
    Weights = Roots/(((n+1)**2)*((polyla(Roots))**2))
    
    return Weights
def funcion(x):
    num=((x**3)*(np.exp(x)-1))/((np.exp(x)-2+(1/np.exp(x))))
    
    return num


def inte(n):
    I = 0
    pesos=GetWeightsGLag(n)
    raices=GetAllRootsGLag(n)
    for i in range(n):
      I += pesos[i]*funcion(raices[i])
    return I

n=6
exis=[]
yes=[]
for i in range(9):
    y=(inte(i+2)/(np.pi**4/15))
    yes.append(y)
    exis.append(i+2)
plt.plot(exis,yes,color="blue",markersize=10)
plt.show()





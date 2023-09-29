import numpy as np
import sympy as sym
x = sym.Symbol('x',real=True)
y = sym.Symbol('y',real=True)
def GetLaguerre(n,x):
    
    y = (sym.exp(-x)*(x**n))
    
    poly = sym.diff( y,x,n )*(sym.exp(x)/np.math.factorial(n))
    
    return poly


def GetDLaguerre(n,x):
    Pn = GetLaguerre(n,x)
    return sym.diff(Pn,x,1)
def GetNewton(f,df,xn,itmax=10000,precision=1e-15):
    
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
def GetRoots(f,df,x,tolerancia = 4):
    
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
n=20

print(GetAllRootsGLag(n))
print(GetWeightsGLag(n))



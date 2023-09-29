import sympy as sym
import numpy as np
x = sym.Symbol('x',real=True)
x1 = sym.Symbol('x1',real=True)
x2 = sym.Symbol('x2',real=True)
y = sym.Symbol('y',real=True)
#a
def get(n,x,y):
    
    y = (x**n*sym.exp(-x))
    
    poly = sym.exp(x)*sym.diff( y,x,n )/np.math.factorial(n)
    
    return poly
print(get(2,x,y))
#b
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
def getD(n,x):
    Pn = get(n,x,y)
    return sym.diff(Pn,x,1)
def raices(n):
    limi=n+(n-1)*np.sqrt(n)
    
    xn = np.linspace(0,limi,100)
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(get(i,x,y))
        DLaguerre.append(getD(i,x))
    
    poly = sym.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sym.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots
#c
w1=sym.simplify(sym.integrate(sym.exp(-x)*((x-x2)/(x1-x2)),(x,0,sym.oo)))
'dado que'
print(w1)
'entonces seria la resta de '
w1num=((1-raices(2)[1])/(raices(2)[0]-raices(2)[1]))
print(w1num)

'y el segundo seria'
w2=sym.simplify(sym.integrate(sym.exp(-x)*((x-x1)/(x2-x1)),(x,0,sym.oo)))
'dado que'
print(w2)
'entonces seria la resta de '
w2num=((raices(2)[0]-1)/(raices(2)[0]-raices(2)[1]))
print(w2num)
#d
total=w1num*(raices(2)[0])**3+w2num*(raices(2)[1])**3
print(total)

print(np.polynomial.laguerre.laggauss(2))

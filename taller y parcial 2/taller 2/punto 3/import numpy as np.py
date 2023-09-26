import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

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

    xn = np.linspace(0,limi,100)
    
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

def GetHermite(n,x):

    if n==0:
        poly = sym.Number(1)
    elif n==1:
        poly = 2*x
    else:
        poly =2*x*GetHermite(n-1,x)-2*(n-1)*GetHermite(n-2,x)
    return sym.expand(poly,x)

def GetDHermite(n,x):
    Pn = GetHermite(n,x)
    return sym.diff(Pn,x,1)
    
def GetAllRootsGHer(n):
    limi=np.sqrt(4*n+1)

    xn = np.linspace(-limi,limi,1000)
    
    Hermite = []
    DHermite = []
    
    for i in range(n+1):
        Hermite.append(GetHermite(i,x))
        DHermite.append(GetDHermite(i,x))
    
    poly = sym.lambdify([x],Hermite[n],'numpy')
    Dpoly = sym.lambdify([x],DHermite[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGHer(n):

    Roots = GetAllRootsGHer(n)
    Hermite = []
    
    for i in range(n):
        Hermite.append(GetHermite(i,x))
    
    polyla = sym.lambdify([x],Hermite[n-1],'numpy')
    Weights = (2**(n-1)*np.math.factorial(n)*np.sqrt(np.pi))/(n**2*(polyla(Roots))**2)
    
    return Weights

def funci(M,R,T,x):
    return 4*(np.pi)*(((M)/(2*(np.pi)*R*T))**(3/2))*(x**2)*(np.e**((-M*(x**2))/(2*R*T)))

#1
def inte(n):
 raices=GetAllRootsGLag(n)
 pesos=GetWeightsGLag(n)
 print(raices)
 print(pesos)
 M=1
 R=1
 T=1
 I = 0
 for i in range(n-1):
    I += pesos[i]*funci(M,R,T,raices[i])
 return I
#2
M=1
R=1
T=1
I = 0

u=np.linspace(1,10,10)
T_values=np.linspace(1,100,10)
for a in T_values:
    y = funci(M,R,a,u)
    plt.plot(u, y, label=f'T = {a}')
#3
def funcimed(M,R,T,x):
    return 4*(np.pi)*(((M)/(2*(np.pi)*R*T))**(3/2))*(x**3)*(np.e**((-M*(x**2))/(2*R*T)))

def inteavg(n,T):
 raices=GetAllRootsGLag(n)
 pesos=GetWeightsGLag(n)

 M=1
 R=1
 I = 0
 for i in range(n-1):
    I += pesos[i]*funcimed(M,R,T,raices[i])
 return I
avlu=[]
for a in T_values:    
    y = inteavg(5,a)
    avlu.append(y)
    
#4
def funcirms(M,R,T,x):
    return 4*(np.pi)*(((M)/(2*(np.pi)*R*T))**(3/2))*(x**4)*(np.e**((-M*(x**2))/(2*R*T)))

def interms(n,T):
 raices=GetAllRootsGLag(n)
 pesos=GetWeightsGLag(n)

 M=1
 R=1
 I = 0
 for i in range(n-1):
    I += pesos[i]*funcimed(M,R,T,raices[i])
 return I
tavr=[]
for a in T_values:    
    y = interms(5,a)
    tavr.append(y)
    
plt.plot(u, tavr)
plt.legend()
plt.show()








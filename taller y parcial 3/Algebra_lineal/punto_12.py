from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import numpy as np
from IPython.display import clear_output
G1= np.array([lambda x,y: np.log(x**2+y**2)-np.sin(x*y)-np.log(2)-np.log(np.pi),
     lambda x,y: np.exp(x-y)+np.cos(x*y)])
def GetF1(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1])
        
    return v
def GetJacobian1(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
            rf = r.copy()
            rb = r.copy()
            
            rf[j] = rf[j] + h
            rb[j] = rb[j] - h
            
            J[i,j] = ( f[i](rf[0],rf[1]) - f[i](rb[0],rb[1])  )/(2*h)
            
    
    return J
#decenso gradeinte 1
def Metric1(G,r):
    return 0.5*np.linalg.norm(GetF1(G,r))**2
def Minimizer1(G,r,lr=1e-2,epochs=int(1e4),error=1e-7):
    
    metric = 1
    it = 0
    
    M = np.array([])
    R = np.array([r])
    
    while metric > error and it < epochs:
        
        M = np.append(M,Metric1(G,r))
        
        J = GetJacobian1(G,r)
        Vector = GetF1(G,r)
        
        # Machine learning
        r -= lr*np.dot(J,Vector)
        
        R = np.vstack((R,r))
        
        metric = Metric1(G,r)
        
        it += 1
    
    return r
#newtonrapshon 1

def NewtonRaphson1(G,r,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.

    while d > error and it < itmax:
        
        rc = r
        
        F = GetF1(G,rc)
        J = GetJacobian1(G,rc)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot(InvJ,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        it += 1

    return r

G2 = np.array([lambda x,y,z: 6*x - 2*np.cos(y*z) - 1.,
     lambda x,y,z: 9*y + np.sqrt( x**2 + np.sin(z) + 1.06 ) + 0.9,
     lambda x,y,z: 60*z + 3*np.exp(-x*y)+10*np.pi - 3])
def GetF2(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1],r[2])
        
    return v
def GetJacobian2(f,r,h=1e-6):
    
    n = r.shape[0]
    
    J = np.zeros((n,n))
    
    for i in range(n):
        for j in range(n):
            
             rf = r.copy()
             rb = r.copy()
            
             rf[j] = rf[j] + h
             rb[j] = rb[j] - h
            
             J[i,j] = ( f[i](rf[0],rf[1],rf[2]) - f[i](rb[0],rb[1],rb[2])  )/(2*h)
            
    
    return J

#decenso gradeinte
def Metric2(G,r):
    return 0.5*np.linalg.norm(GetF2(G,r))**2
def Minimizer2(G,r,lr=1e-4,epochs=10000,error=1e-7):
    
    metric = 1
    it = 0
    
    M = np.array([])
    R = np.array([r])
    
    while metric > error and it < epochs:
        
        M = np.append(M,Metric2(G,r))
        
        J = GetJacobian2(G,r)
        Vector = GetF2(G,r)
        
        # Machine learning
        r -= lr*np.dot(J,Vector)
        
        R = np.vstack((R,r))
        
        metric = Metric2(G,r)
        
        it += 1
    
    return r
#newtonrapshon

def NewtonRaphson2(G,r,itmax=1000,error=1e-9):
    
    it = 0
    d = 1.

    while d > error and it < itmax:
        
        rc = r
        
        F = GetF2(G,rc)
        J = GetJacobian2(G,rc)
        InvJ = np.linalg.inv(J)
        
        r = rc - np.dot(InvJ,F)
        
        diff = r - rc
        
        d = np.max( np.abs(diff) )
        
        it += 1

    return r
print(NewtonRaphson1(G1,np.array([2.,2.])))
print(Minimizer1(G1,np.array([2.,2.])))
print(NewtonRaphson2(G2,np.array([1.,1.,1.])))
print(Minimizer2(G2,np.array([1.,1.,1.])))

from IPython.display import display, HTML
display(HTML("<style>.container { width:100% !important; }</style>"))
import numpy as np
from IPython.display import clear_output
q=3*10**-4
w=114.6
k=8.9*10**9
l=5
G1= np.array([lambda x,y: x*np.cos(y)-114.6,
     lambda x,y: -x*np.sin(y)+(k*q**2/(2*l*np.sin(y))**2)+np.sqrt(2)*(k*q**2/(np.sqrt(2)*l*np.sin(y))**2)])
def GetF1(G,r):
    
    n = r.shape[0]
    
    v = np.zeros_like(r)
    
    for i in range(n):
        v[i] = G[i](r[0],r[1])
        
    return v
def GetJacobian1(f,r,h=1e-7):
    
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
#newtonrapshon 1

def NewtonRaphson1(G,r,itmax=6000,error=1e-10):
    
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
T,thea=NewtonRaphson1(G1,np.array([2.,2.]))
thea+=2*np.pi
angu=thea*180/np.pi
print(T,angu)
print(-143.04793329*np.sin(0.6416152962179433)+(k*q**2/(2*l*np.sin(0.6416152962179433))**2)+np.sqrt(2)*(k*q**2/(np.sqrt(2)*l*np.sin(0.6416152962179433))**2))

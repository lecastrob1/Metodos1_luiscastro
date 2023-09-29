import numpy as np
import sympy as sym
x = sym.symbols('x',real=True)

# con funces de prueba ya que mi computadora se demora demasiado en cargar

def funcion(x,T,difT):
    raiz=x**2+difT**2
    num=np.tanh((np.sqrt(raiz)*300)/(2*T))
    return 0.5*num/np.sqrt(raiz)
def valortc():
    T=0.1
    h=1e-4
    nodes, weights = np.polynomial.legendre.leggauss(50)
    Tc = 0.
    error = 1
    while T < 20 and error > h:
        
        appr = np.sum(weights * funcion(nodes,T,0.))
        error =  np.abs(np.abs(appr)-10./3)
            
        Tc = T
        T += 0.0001
        
    return Tc

print(valortc())


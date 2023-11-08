import numpy as np
 
def f(x):
    return np.abs(x-2)
Dx = lambda f,x,h=1e-5: (f(x+h) - f(x-h))/(2*h)
def Minimizer(f, N=100000, gamma=0.0001):
    
    r = np.zeros(N)
    # Seed
    r[0] = np.random.uniform(-5,5)
    
    for i in range(1,N):
        r[i] = r[i-1] - gamma*Dx(f,r[i-1])
    return r
x = Minimizer(f)
print(x[-1])
#aunque se pueda acercar el gradiente al punto mínimo la función aunque sea continua no es diferenciable en el punto a observar por lo que realmente aunque este muy cerca nunca dara el valor
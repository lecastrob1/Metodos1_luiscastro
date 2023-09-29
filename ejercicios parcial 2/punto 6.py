import numpy as np

def funcion(x):
    a=0.01
    R=0.5
    num=np.sqrt(a**2-x**2)
    dem=R+x
    return num/dem

x=np.linspace(-0.01,0.01,1000)
h=x[1]-x[0]
def inte_trape(f,x,h):
    tota=0
    tota+=h/2*(f(x[0])+f(x[-1]))
    for i in range(1,len(x)-1):
        tota+=h*f(x[i])
    return tota
def sims13(f,x,h):
    tota=0
    tota+=(f(x[0])+f(x[-1]))
    for i in range(1,len(x)-1):
        tota+=4*f(x[i])    
    return h/3*tota
def exac():
    return 
def err():
    valort=inte_trape(funcion,x,h)
    valor13=sims13(funcion,x,h)
    errt=np.abs(valort-(np.pi*(0.5-np.sqrt((0.5)**2-(0.01)**2))))/(np.pi*(0.5-np.sqrt(0.5**2-0.01**2)))
    err13=np.abs(valor13-(np.pi*(0.5-np.sqrt((0.5)**2-(0.01)**2))))/(np.pi*(0.5-np.sqrt(0.5**2-0.01**2)))
    a=[errt,err13]
    return a
print('el valor con el metodo trapecio es',inte_trape(funcion,x,h))
print('el valor con el metodo simson1/3 es',sims13(funcion,x,h))
print('el error del metodo de trapecio es',(err())[0],'y simson 1/3 es',(err())[1])

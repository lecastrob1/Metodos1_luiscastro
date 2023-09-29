import numpy as np
h=6.626*10**(-34)
k=1.3806*10**(-23)
c=3*10**8
T=5772
lam0=100
lam1=400
def funnum(x):
    num=x**3
    dem=np.exp(x)-1
    return num/dem
def fundem(x):
    num=x**3
    dem=1-np.exp(-x)
    return num/dem
b=(h*(c/(lam1*10**(-9))))/(k*T)
a=(h*(c/(lam0*10**(-9))))/(k*T)
#a
def totanum():
    
    print('lim b',b)
    print('lim a',a)
    nodesle, weightsle = np.polynomial.legendre.leggauss(20)
    tota=0   
    tota=np.sum(weightsle*funnum(0.5*(nodesle*(a-b)+a+b)))
    return 0.5*(a-b)*tota
#b
def totadem():
 nodesla, weightsla = np.polynomial.laguerre.laggauss(20)
 tota=0
 tota=np.sum(weightsla * fundem(nodesla))
 return tota
#c
print('los limites de integracion inferior es',str(b),'y el superiro es',str(a))
#d
print('la fraccion porcentual es',str(totanum()/totadem()))
#e
'debido a que la longitud de onda de los rayos ultraviolate son menores dando asi una mayor v '
'y aumentando tanto el limite superior como inferior de integración, pero como la funcion decae '
'exponencialmente al final la integracion sera mucho menor dando una menor relación'
'tambien al tener una menor longiutd de onda lo dfracta el agua de manera que se disipa mucho mas'
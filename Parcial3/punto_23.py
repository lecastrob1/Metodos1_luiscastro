import numpy as np
A=np.array([[1/5.,1/10.,1.,1.,0. ],
          [1/10.,4.,-1.,1.,-1.],
          [1.,-1.,60.,0.,-2.],
          [1.,1.,0.,8.,4.],
          [0.,-1.,-2.,-4.,700.]])
b=np.array([1,2,3,4,5])
def grad (A,b,x0,e=0.01):
    r0=np.dot(A, x0) - b
    p0=-r0
    k=0
    d=1

    while d > e:
                
        # Vector actual
        x=x0
        r = r0
        pn=p0
        alp=-(np.dot(r.T,pn))/(np.dot((np.dot(pn.T,A)),pn))
        x0=x+np.dot(alp,pn)
        r0=np.dot(A,x0)-b
        beta=(np.dot((np.dot(r0.T,A)),pn))/(np.dot((np.dot(pn.T,A)),pn))
        p0=-r0+np.dot(beta,pn)

        
        diff = r0 - r
        
        d = np.max( np.abs(diff) )
        k+=1
    return k,x
x0=np.array([1.,1.,1.,1.,1.])
print( grad (A,b,x0))
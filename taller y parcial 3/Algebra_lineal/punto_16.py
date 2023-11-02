import numpy as np
import sympy as sym

gamma0=np.array([[1.,0.,0.,0.],
                  [0,1.,0.,0.],
                  [0.,0.,-1.,0.],
                  [0.,0.,0.,-1.]])
gamma1=np.array([[0.,0.,0.,1.],
                  [0,0.,1.,0.],
                  [0.,-1.,0.,0.],
                  [-1.,0.,0.,0.]])
gamma2=np.array([[0.,0.,0.,(-1)*sym.I],
                  [0,0.,sym.I,0.],
                  [0.,sym.I,0.,0.],
                  [(-1)*sym.I,0.,0.,0.]])
gamma3=np.array([[0.,0.,1.,0.],
                  [0,0.,0.,-1.],
                  [-1.,0.,0.,0.],
                  [0.,1.,0.,0.]])
matrices=[gamma0, gamma1, gamma2, gamma3]
N=np.zeros((4,4))
for i in range(4):
    for j in range(4):
     print(i,j)
     print(np.dot(matrices[j],matrices[i])+np.dot(matrices[i],matrices[j]))


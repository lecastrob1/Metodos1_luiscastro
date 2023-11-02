
import numpy as np
import sympy as sym

sigmax=np.array([[0.,1.],
                [1.,0.]])
sigmay=np.array([[0.,(-1)*sym.I],
                [sym.I,0.]])
sigmaz=np.array([[1.,0.],
                [0.,-1.]])
matrices=[sigmax,sigmay,sigmaz]
for i in range(3):
    for j in range(3):
        print(i,j)
        print(np.dot(matrices[i],matrices[j])-np.dot(matrices[j],matrices[i]))
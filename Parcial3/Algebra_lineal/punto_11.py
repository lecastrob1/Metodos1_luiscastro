import numpy as np

A= np.array([[1,2,-1],
             [1,0,1],
             [4,-4,5]])
q=np.array([1.,0.,0.])



def valgrand(A,q):
 k = 200

 mu = 0


 for i in range(k):

  z = np.linalg.solve(A , q)
  q = z / np.linalg.norm(z)
  mu = np.dot(q.T, np.dot(A, q))
 return mu,q
# Mostrar el resultado
delta,Q=valgrand(A,q)
print("El valor propio aproximado es:", delta)
print("El vector propio asociado es:", Q)


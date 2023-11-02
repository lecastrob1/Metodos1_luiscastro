import numpy as np
import scipy.linalg as la

A= np.array([[-2.,1.,0.],
             [1.,-2.,1.],
             [0.,1,-2.]])
# Definir el vector inicial q
q=np.array([5.,3.,2.])
sigma = 1e-10

k = 200

mu = 0


for i in range(k):
  z = np.linalg.solve(A , q)
  q = z / np.linalg.norm(z)
  mu = np.dot(q.T, np.dot(A, q))
delta=mu
# Mostrar el resultado
print("El valor propio mayor aproximado es:", delta)
print("El vector propio asociado es:", q)

def valpeq(A,q):
 k = 300

 mu = 0

 nueA=np.linalg.inv(A)
 for i in range(k):

  z = np.linalg.solve(nueA , q)
  q = z / np.linalg.norm(z)
  mu = np.dot(q.T, np.dot(A, q))

 return mu,q

delta1,Q1=valpeq(A,np.array([-10.,-10.,-10.]))
print("El valor propio menor aproximado es:", delta1)
print("El vector propio asociado es:", Q1)

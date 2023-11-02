import numpy as np
#punto 1
def multiplicar_matrices(A, B):
    if len(A[0])==len(B):
     C = np.zeros(((len(A),len(B[0]))))

     for i in range(len(A)):
      for j in range(len(B[0])):
   
        for k in range(len(B)):
          C[i][j] += A[i][k] * B[k][j]
    else:
      print("no se puede ya que las columnas y las filas tiene diferentes dimenciones")
      return
    return C
#puntoa
A=np.array([[5.,-4.,-2.],
            [5.,-5.,4.],
            [2.,5.,-4.],
            [-5.,4.,3.],
            [3.,-4.,-3.]])
B=np.array([[5.],
            [-2.],
            [-3.]])

print(multiplicar_matrices(A, B))
#puntob
C=np.array([[0.,-1.,-1.,3.],
            [5.,-5.,-2.,2.],
            [1.,0.,4.,5.]])
D=np.array([[0.,-3],
            [-2.,-1.],
            [3.,-3.]])
print(multiplicar_matrices(C, D))
#puntoc
E=np.array([[2.,-5.,5.,1.],
            [5.,2.,-7.,-6.],
            [-6.,-1.,7.,-4.],
            [5.,4.,1.,-5.]])
F=np.array([[0.,4.,-7.,1.,-6.],
            [-1.,-6.,-5.,1.,1.],
            [2.,-1.,-6.,5.,-5.],
            [-3.,-6.,6.,3.,5.]])
print(multiplicar_matrices(E, F))
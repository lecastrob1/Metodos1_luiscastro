import numpy as np

A=np.array([[1.,0.,0.],
                  [5.,1.,0.],
                  [-2.,3.,1.]])
B=np.array([[4.,-2.,1.],
                  [0,3.,7.],
                  [0.,0.,2.]])

def multiplicar_matrices(A, B):
    C = np.zeros(((len(A),len(B[0]))))

    for i in range(len(A)):
      for j in range(len(B[0])):
   
        for k in range(len(B)):
          C[i][j] += A[i][k] * B[k][j]

    return C
print(multiplicar_matrices(A, B))
import numpy as np
#reudccion gaussiana
def gaussian_elimination(A: np.array,b: np.array):
    '''
    Args:
        A (np.array): Matriz de coeficientes cuadrada (n x n).
        b (np.array): Vector de constantes de longitud n

    Returns:
        M (np.array): Matriz aumentada [A|b] reducida utilizando el algoritmo de eliminación Gaussiana
    '''
    n = np.shape(A)[0]
    M = np.zeros(shape=(n,n+1))
    M[:,0:n] = A
    M[:,n] = b
    for i in range (1,n):
        for j in range(0,i):
            C=(M[i,j]/M[j,j])
            M[i,:]=M[i,:]-C*M[j,:]
    matrizA=np.delete(M, -1, axis=1)
    matrizb=np.take(M, -1, axis=1)
    matrizx=np.zeros((1,len(A[0])))
    sub0=len(A[0])-1
    matrizx[0][sub0]=matrizb[sub0]/matrizA[sub0][sub0]
    for i in range(len(matrizA[0])-2,-1,-1):
     matrizx[0][i] = (matrizb[i] - sum(matrizA[i][j] * matrizx[0][j] for j in range(sub0, i, -1))) / matrizA[i][i]


    return matrizx
#puntoa
A = np.array([[3.,1.,-1.],
              [1.,-2.,1.],
              [4.,-1.,1.]])
b = np.array([2.,0.,3.])

print(gaussian_elimination(A,b))
#puntob
C = np.array([[1.,1.,1.],
              [0.,-8.,10.],
              [4.,-8.,0.]])
d = np.array([0.,0.,6.])
print(gaussian_elimination(C,d))

import numpy as np

def SOR(A, b, omega, inicio, convergence_criteria=1e-8):
    """
    A function to perform Successive Over-Relaxation (SOR) method.
    """
    phi = inicio[:]
    residual = np.linalg.norm(np.matmul(A, phi) - b)  # Initial residual
    it=0
    while residual > convergence_criteria:
        for i in range(A.shape[0]):
            sigma1 = 0
            sigma2 = 0
            for j in range(i):
                sigma1 += A[i][j] * phi[j]
            for j in range(i+1, A.shape[1]):
                sigma2 += A[i][j] * phi[j]
            phi[i] = (1 - omega) * phi[i] + (omega / A[i][i]) * (b[i] - sigma1 - sigma2)
        residual = np.linalg.norm(np.matmul(A, phi) - b)
        it+=1
    return phi, it


# Ejemplo de uso:
A = np.array([[3, -1, -1],
              [-1, 3, 1],
              [2, 1, 4]])

b = np.array([1, 3, 7])
omega =0.96 # Valor de sobre relajación
inicio = np.zeros(len(b))

phi, it = SOR(A, b, omega, inicio)
print('Solución: ', phi)
print('iteraicones', it)



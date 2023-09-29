import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def integrate(n):
    # Crear la grilla
    matr=np.zeros((n+1,n+1))
    for i in range(n+1):
        for j in range(n+1):
            val=1-(i**2/n**2)-(j**2/n**2)
            if val>=0:
                matr[i][j]=np.sqrt(val)

    xis=len(matr)
    yis=len(matr[0])            
    volume = 0.0
    for i in range(xis-1):
        for j in range(yis-1):
            # Calcular el promedio de la función en los cuatro vértices
            avg_value = (matr[i][j]) + matr[i+1][j]+matr[i][j+1]+matr[i+1][j+1]
            
            # Sumar al volumen total
            volume += avg_value/n**2

    return volume



# Número de cuadrados en cada lado de la grilla
n = 100

# Calcular el volumen
volume = integrate(300)
print("El volumen de la semiesfera es:", volume)

def f2(x,y,R):

    if np.sqrt(x**2 + y**2) > R**2:
        return 0.
    else:
        return np.sqrt(x**2 + y**2)

R=1
x = np.linspace(-R,R,10)
y = x.copy()

X,Y = np.meshgrid(x,y)
Z = np.zeros_like(X)

for i in range(len(x)):
    for j in range(len(y)):
        Z[i,j] = f2(x[i],y[j],R)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(X,Y,Z)
plt.show()
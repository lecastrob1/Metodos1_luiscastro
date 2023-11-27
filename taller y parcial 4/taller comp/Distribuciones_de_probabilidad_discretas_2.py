import numpy as np

# a) Encuentre el menor valor de n tal que la probabilidad de que haya al menos n desconexiones en menos de un per´ıodo de 4 horas es menor que 0.01.
mu = 1  # tasa de desconexiones por período de 4 horas
n = 0
while True:
    prob = 1 - np.sum(np.exp(-mu) * mu**np.arange(n) / np.cumprod(np.arange(1, n+1)))
    if prob < 0.01:
        break
    n += 1
print(f'a) El menor valor de n es {n}')

# b) Encuentre el menor valor del n´umero de horas h tal que la probabilidad de que no haya desconexiones en h horas sea menor que 0.02.
h = 0
while True:
    mu_h = h / 4  # tasa de desconexiones por h horas
    prob = np.exp(-mu_h)
    if prob < 0.02:
        break
    h += 1
print(f'b) El menor valor de h es {h} horas')

# c) Encuentre la probabilidad de que en 3 per´ıodos consecutivos de 4 horas, haya solamente un per´ıodo de 4 horas sin desconexiones.
mu_3 = 3 * mu  # tasa de desconexiones por 3 períodos de 4 horas
prob_c = 3 * np.exp(-mu) * mu * np.exp(-2*mu)  # 2 desconexiones en 3 períodos de 4 horas
print(f'c) La probabilidad es {prob_c}')

# d) Encuentre la probabilidad de que el n´umero de desconexiones en 3 per´ıodos consecutivos de 4 horas sea igual al n´umero esperaod de desconexiones en 3 per´ıodos consecutivos de 4 horas.
prob_d = np.exp(-mu_3) * mu_3**mu_3 / np.prod(np.arange(1, mu_3+1))  # número de desconexiones es igual al número esperado
print(f'd) La probabilidad es {prob_d}')

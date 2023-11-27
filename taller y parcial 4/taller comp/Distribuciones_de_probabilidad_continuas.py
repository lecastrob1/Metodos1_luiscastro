import numpy as np

# Definimos la función de densidad de probabilidad
def f(x):
    return np.where((-1 <= x) & (x <= 2), x**2/3, 0)

# Definimos los límites de las probabilidades que queremos calcular
limites = [(0, 1), (1, 2)]

# Calculamos las probabilidades
for i, (lim_inf, lim_sup) in enumerate(limites):
    x = np.linspace(lim_inf, lim_sup, 1000)
    prob = np.trapz(f(x), x)
    print(f'P({lim_inf} < X ≤ {lim_sup}) = {prob}')
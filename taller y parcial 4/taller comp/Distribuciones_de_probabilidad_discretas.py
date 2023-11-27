import numpy as np
import math

# Función para calcular el coeficiente binomial
def binom_coef(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

# Función para calcular la probabilidad binomial
def binom_prob(n, k, p):
    return binom_coef(n, k) * (p**k) * ((1 - p)**(n - k))

# Planes de muestreo
planes = [(5, 1), (25, 5)]

# Rango de p
p_values = np.linspace(0, 1, 100)

# Para cada plan de muestreo
for n, a in planes:
    # Calcula las probabilidades de aceptación para cada valor de p
    prob_aceptacion = [sum(binom_prob(n, i, p) for i in range(a + 1)) for p in p_values]
    
    # Imprime las probabilidades de aceptación
    print(f"Plan de muestreo: n={n}, a={a}")
    print("Probabilidades de aceptación:")
    for p, prob in zip(p_values, prob_aceptacion):
        print(f"p={p:.2f}: {prob:.2f}")

#a) si fuece un vendedor que produce lotes con una fracción defectuosa que va de p = 0ap = ,10 elegiria el de n=25, a=5 ya que tiene mayor probabilidad de aceptación
#b)Si usted fuera un comprador que desea protegerse contra la aceptación de lotes con una fracción defectuosa que exceda de p = ,30 elegiria el de n=25, a=5 ya que tiene menor probabilidad de aceptación siendo mas seguro para la compra
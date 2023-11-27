import numpy as np

# Definimos los parámetros de la distribución
media = 78
varianza = 36
desviacion_estandar = np.sqrt(varianza)

# Función de distribución acumulativa para una distribución normal
def cdf(x, media, desviacion_estandar):
    z = (x - media) / desviacion_estandar
    return 0.5 * (1 + np.tanh(np.sqrt(np.pi/8) * z))

# Función de cuantil (inversa de la CDF) para una distribución normal
def ppf(q, media, desviacion_estandar):
    z = np.sqrt(8/np.pi) * np.arctanh(2*q - 1)
    return media + desviacion_estandar * z

# a) Probabilidad de que una persona alcance calificaciones mayores de 72
prob_a = 1 - cdf(72, media, desviacion_estandar)
print(f'a) La probabilidad de obtener una calificación mayor a 72 es {prob_a:.2f}')

# b) Calificación mínima para estar en el 10% más alto
calif_b = ppf(0.9, media, desviacion_estandar)
print(f'b) La calificación mínima para estar en el 10% más alto es {calif_b:.2f}')

# c) Punto límite para pasar el examen si se desea pasar al 28.1% más alto
punto_c = ppf(1 - 0.281, media, desviacion_estandar)
print(f'c) El punto límite para pasar el examen es {punto_c:.2f}')

# d) Proporción de estudiantes con calificaciones 5 puntos arriba del 25% más bajo
punto_d = ppf(0.25, media, desviacion_estandar) + 5
prop_d = 1 - cdf(punto_d, media, desviacion_estandar)
print(f'd) La proporción de estudiantes con calificaciones 5 puntos arriba del 25% más bajo es {prop_d:.2f}')

# e) Si la calificación de un estudiante excede de 72, ¿cuál es la probabilidad de que su calificación exceda de 84?
prob_e = (1 - cdf(84, media, desviacion_estandar)) / (1 - cdf(72, media, desviacion_estandar))
print(f'e) La probabilidad de que la calificación exceda de 84 dado que ya excedió de 72 es {prob_e:.2f}')

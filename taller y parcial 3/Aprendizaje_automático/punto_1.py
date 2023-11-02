import numpy as np
import sympy as sym
 
# Definir las variables
x, y = sym.symbols('x y')

# Definir la función
f = x**2 - y**2 + 2*x

# Calcular las derivadas parciales
dx = sym.diff(f, x)
dy = sym.diff(f, y)

# Evaluar las derivadas parciales en el punto (x0, y0)
x0 = 1
y0 = 1
grad_f_x0_y0 = [dx.subs({x: x0, y: y0}), dy.subs({x: x0, y: y0})]

# Calcular el valor de la función en el punto (x0, y0)
f_x0_y0 = f.subs({x: x0, y: y0})

# Definir el plano tangente
tangent_plane = f_x0_y0 + grad_f_x0_y0[0] * (x - x0) + grad_f_x0_y0[1] * (y - y0)

print("El plano tangente es: ", tangent_plane)

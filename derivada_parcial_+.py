from os import system
from sympy import symbols, sin, cos, exp, diff

# Definimos las variables simbólicas
x, y, λ, C1, C2 = symbols('x y λ C1 C2')

# Definimos la función
H = exp(-λ*x) * (C1*sin(λ*y) + C2*cos(λ*y))

# Calculamos las derivadas parciales
dH_dx = diff(H, x)
dH_dy = diff(H, y)

dH_dx_x = diff(dH_dx, x)
dH_dy_y = diff(dH_dy, y)

y_2__x_2 = dH_dx_x+dH_dy_y
# Imprimimos los resultados
system("cls")
print('funcion escalar')
print('H = e^(-λx)*(C1*sin(λy) + C2*sin(λy))\n')
print("d^2H/dx^2:")
print(dH_dx_x)

print("\nd^2H/dy^2:")
print(dH_dy_y)
print("\nSuma de las derivadas parciales:")
print(f'{y_2__x_2} = 0')


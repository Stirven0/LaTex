from os import system
import sympy as sp

# Definir las variables
x, y, z = sp.symbols('x y z')

# Definir el campo vectorial A
A = sp.Matrix([2*x**2, -3*z*y, x*z**2])

# Definir el operador gradiente y calcular la divergencia
grad = sp.Matrix([[sp.diff(f, var) for var in (x, y, z)] for f in A])
div_A = sp.diff(A[0], x) + sp.diff(A[1], y) + sp.diff(A[2], z)

# Calcular el rotacional
rot_A = sp.Matrix([
    sp.diff(A[2], y) - sp.diff(A[1], z),
    sp.diff(A[0], z) - sp.diff(A[2], x),
    sp.diff(A[1], x) - sp.diff(A[0], y)
])
system("cls")
print(f'Funcion escalar')
print(f'A = A=2²i-3zyj+xz²k\n')
print(f"Divergencia de A: {div_A}")
print(f"Rotacional de A: {rot_A}")

import sympy as sp

# Definimos las variables simbólicas
x, y, z = sp.symbols('x y z')

# Definimos los componentes de la función vectorial A
A_i = sp.cos(x * y)  # Componente i
A_j = 3 * x * y - 2 * x**2  # Componente j
A_k = - (3 * x + 2 * y)  # Componente k

# Calculamos las derivadas parciales con respecto a x, y, z para cada componente

# Para A_i (componente i)
partial_Ai_x = sp.diff(A_i, x)
partial_Ai_y = sp.diff(A_i, y)
partial_Ai_z = sp.diff(A_i, z)

# Para A_j (componente j)
partial_Aj_x = sp.diff(A_j, x)
partial_Aj_y = sp.diff(A_j, y)
partial_Aj_z = sp.diff(A_j, z)

# Para A_k (componente k)
partial_Ak_x = sp.diff(A_k, x)
partial_Ak_y = sp.diff(A_k, y)
partial_Ak_z = sp.diff(A_k, z)

# Mostramos los resultados
print(f"Derivadas parciales de A_i = cos(xy):")
print(f"d(A_i)/dx: {partial_Ai_x}")
print(f"d(A_i)/dy: {partial_Ai_y}")
print(f"d(A_i)/dz: {partial_Ai_z}\n")

print(f"Derivadas parciales de A_j = 3xy - 2x^2:")
print(f"d(A_j)/dx: {partial_Aj_x}")
print(f"d(A_j)/dy: {partial_Aj_y}")
print(f"d(A_j)/dz: {partial_Aj_z}\n")

print(f"Derivadas parciales de A_k = -(3x + 2y):")
print(f"d(A_k)/dx: {partial_Ak_x}")
print(f"d(A_k)/dy: {partial_Ak_y}")
print(f"d(A_k)/dz: {partial_Ak_z}")


# A = cos(xy)i+[3xy-2y]j-[3x+2y]k
# d(A)/dx = -ysin(xy)i+[-4x+3y]j-[-3]K
# d(A)/dy = -ysin(xy)i+[-4x+3y]j-[-3]K
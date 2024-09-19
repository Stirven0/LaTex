from os import system
import sympy as sp

# Definimos las variables simbólicas
x, y, z = sp.symbols('x y z')

# Definimos los componentes de la función vectorial A
A_i = sp.cos(x * y)
A_j = 3 * x * y - 2 * x**2 
A_k = - (3 * x + 2 * y)

# Calculamos las derivadas parciales con respecto a x, y, z para cada componente

# derivadas parciales de primer nivel
# Para A_i (componente i)
partial_Ai_x = sp.diff(A_i, x)
partial_Ai_y = sp.diff(A_i, y)

# Para A_j (componente j)
partial_Aj_x = sp.diff(A_j, x)
partial_Aj_y = sp.diff(A_j, y)

# Para A_k (componente k)
partial_Ak_x = sp.diff(A_k, x)
partial_Ak_y = sp.diff(A_k, y)


# derivadas parciales de segundo nivel
# Para A_i (componente i)
partial_Ai_x_x = sp.diff(partial_Ai_x, x)
partial_Ai_y_y = sp.diff(partial_Ai_y, y)

# Para A_j (componente j)
partial_Aj_x_x = sp.diff(partial_Aj_x, x)
partial_Aj_y_y = sp.diff(partial_Aj_y, y)

# Para A_k (componente k)
partial_Ak_x_x = sp.diff(partial_Ak_x, x)
partial_Ak_y_y = sp.diff(partial_Ak_y, y)

# Derivadas parciales crusadas 
# Para A_i (componente i)
partial_Ai_x_y = sp.diff(partial_Ai_x, y)
partial_Ai_y_x = sp.diff(partial_Ai_y, x)

# Para A_j (componente j)
partial_Aj_x_y = sp.diff(partial_Aj_x, y)
partial_Aj_y_x = sp.diff(partial_Aj_y, x)

# Para A_k (componente k)
partial_Ak_x_y = sp.diff(partial_Ak_x, y)
partial_Ak_y_x = sp.diff(partial_Ak_y, x)

system("cls")

print(f'Funcion A = cos(xy)i+[3xy-2y]j-[3x+2y]k\n')
print(f'Derivada parcial d(A)/dx =[{partial_Ai_x}]i+[{partial_Aj_x}]j+[{partial_Ak_x}]k')
print(f'Derivada parcial d(A)/dy =[{partial_Ai_y}]i+[{partial_Aj_y}]j+[{partial_Ak_y}]k')
print(f'Derivada parcial d^2(A)/dx^2 =[{partial_Ai_x_x}]i+[{partial_Aj_x_x}]j+[{partial_Ak_x_x}]k')
print(f'Derivada parcial d^2(A)/dy^2 =[{partial_Ai_y_y}]i+[{partial_Aj_y_y}]j+[{partial_Ak_y_y}]k')
print(f'Derivada parcial d^2(A)/dxy =[{partial_Ai_x_y}]i+[{partial_Aj_x_y}]j+[{partial_Ak_x_y}]k')
print(f'Derivada parcial d^2(A)/dyx =[{partial_Ai_y_x}]i+[{partial_Aj_y_x}]j+[{partial_Ak_y_x}]k')

# A = cos(xy)i+[3xy-2y]j-[3x+2y]k
# d(A)/dx = -ysin(xy)i+[-4x+3y]j-[-3]K
# d(A)/dy = -ysin(xy)i+[-4x+3y]j-[-3]K
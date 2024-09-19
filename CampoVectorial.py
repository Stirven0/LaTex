import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir el campo escalar φ(x, y, z)
def funcion_vec(x, y, z):
    return 4 * y * x**3 + 3 * x * y * z - z**2 + 2

# Evaluar φ en el punto (1, -1, -2)
x_val, y_val, z_val = 1, -1, -2
valor_funcion = funcion_vec(x_val, y_val, z_val)

# Crear un espacio de puntos para visualizar el campo escalar
x = np.linspace(-2, 2, 30)
y = np.linspace(-2, 2, 30)
z = np.linspace(-2, 2, 30)
X, Y, Z = np.meshgrid(x, y, z)

# Evaluar el campo escalar en todos los puntos
phi_values = funcion_vec(X, Y, Z)

# Crear la figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar un gráfico de superficies con niveles de campo escalar
ax.contour3D(X[:, :, 0], Y[:, :, 0], phi_values[:, :, 0], 50, cmap='viridis')

# Etiquetas
ax.set_title(f'Campo escalar ϕ(x, y, z) = 4yx³+3xyz-z²+2 \n ϕ(1, -1, -2) = {valor_funcion}')
ax.set_xlabel('X')
ax.set_ylabel('Y')
# ax.set_zlabel('ϕ(x, y, z)')

# Mostrar la gráfica
plt.show()
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Definir los vértices del triángulo
A = np.array([3, 21, 2])
B = np.array([1, 21, 23])
C = np.array([4, 23, 1])

# Calcular dos vectores que forman el triángulo
AB = B - A
AC = C - A

# Calcular el producto cruzado
cross_product = np.cross(AB, AC)

# Calcular el área del triángulo
area = np.linalg.norm(cross_product) / 2

# Representación gráfica del triángulo
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Dibujar los puntos
ax.scatter(*A, color='r', label='A (3, 21, 2)')
ax.scatter(*B, color='g', label='B (1, 21, 23)')
ax.scatter(*C, color='b', label='C (4, 23, 1)')

# Dibujar los lados del triángulo
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='g')
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], color='b')
ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='r')

# Configurar etiquetas y título
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Triángulo en 3D')

# Mostrar leyenda
ax.legend()

# Mostrar el área en la gráfica
ax.text2D(0.05, 0.95, f'Área del triángulo: {area:.2f}', transform=ax.transAxes, fontsize=12, color='black')

# Mostrar gráfico
plt.show()
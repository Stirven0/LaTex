import numpy as np
import matplotlib.pyplot as plt

# Definir los vectores
a = np.array([3, 2, -6])
b = np.array([4, -3, 1])

# Calcular el producto punto
dot_product = np.dot(a, b)

# Calcular las magnitudes de los vectores
magnitude_a = np.linalg.norm(a)
magnitude_b = np.linalg.norm(b)

# Calcular el coseno del ángulo
cos_theta = dot_product / (magnitude_a * magnitude_b)

# Calcular el ángulo en radianes y luego convertir a grados
theta_radians = np.arccos(cos_theta)
theta_degrees = np.degrees(theta_radians)

# Visualización de los vectores
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Origen
origin = [0, 0, 0]

# Graficar los vectores
ax.quiver(*origin, *a, color='r', label='Vector c')
ax.quiver(*origin, *b, color='b', label='Vector d')

# Limites para los ejes
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Mostrar la leyenda y el gráfico
plt.legend()
plt.title(f'Ángulo entre vectores: {theta_degrees:.2f}°')
plt.show()
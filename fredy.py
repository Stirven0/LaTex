import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from os import system

def campo_escalar():
    # Definir el campo escalar φ(x, y, z)
    def funcion_vec(x, y, z):
        return 4 * y * x**3 + 3 * x * y * z - z**2 + 2

    # Menú de selección de puntos
    print("\n--- Evaluar campo escalar en ---")
    print("1. Punto (1, -1, -2)")
    print("2. Punto (0, 3, -1)")
    print("3. Ingresar punto manualmente")
    choice = input("Elige una opción (1-3): ")

    if choice == '1':
        x_val, y_val, z_val = 1, -1, -2
    elif choice == '2':
        x_val, y_val, z_val = 0, 3, -1
    elif choice == '3':
        x_val = float(input("Ingresa el valor de x: "))
        y_val = float(input("Ingresa el valor de y: "))
        z_val = float(input("Ingresa el valor de z: "))
    else:
        print("Opción inválida.")
        return

    # Evaluar la función en el punto seleccionado
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
    ax.set_title(f'Campo escalar ϕ(x, y, z) = 4yx³+3xyz-z²+2 \n ϕ({x_val}, {y_val}, {z_val}) = {valor_funcion}')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('ϕ(x, y, z)')

    # Mostrar la gráfica
    plt.show()

def derivadas_parciales():
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

def area_triangulo():
    # Menú de selección de vértices
    print("\n--- Área del triángulo ---")
    print("1. Vértices [(3,21,2), (1,21,23),(4,23,1)]")
    print("2. Vértices [(2,23,22), (22,3,2), (4,3,21)]")
    print("3. Ingresar vértices manualmente")
    choice = input("Elige una opción (1-3): ")

    if choice == '1':
        A = np.array([3, 21, 2])
        B = np.array([1, 21, 23])
        C = np.array([4, 23, 1])
    elif choice == '2':
        A = np.array([2, 23, 22])
        B = np.array([22, 3, 2])
        C = np.array([4, 3, 21])
    elif choice == '3':
        A = np.array([float(input("Ingresa las coordenadas de A (x, y, z): ")), 
                      float(input()), 
                      float(input())])
        B = np.array([float(input("Ingresa las coordenadas de B (x, y, z): ")), 
                      float(input()), 
                      float(input())])
        C = np.array([float(input("Ingresa las coordenadas de C (x, y, z): ")), 
                      float(input()), 
                      float(input())])
    else:
        print("Opción inválida.")
        return

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
    ax.scatter(*A, color='r', label=f'A {A}')
    ax.scatter(*B, color='g', label=f'B {B}')
    ax.scatter(*C, color='b', label=f'C {C}')

    # Dibujar los lados del triángulo
    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='g')
    ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], color='b')
    ax.plot([B[0], C[0]], [B[1], C[1]], [B[2], C[2]], color='r')

    # Configurar etiquetas y título
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Triángulo en 3D')

    # Mostrar el área en la gráfica
    ax.text2D(0.05, 0.95, f'Área del triángulo: {area:.2f}', transform=ax.transAxes, fontsize=12, color='black')

    # Mostrar gráfico
    plt.show()

def angulo_vectores():
    # Menú de selección de vectores
    print("\n--- Ángulo entre dos vectores ---")
    print("1. Vectores a=(3, 2, -6) y b=(4, -3, 1)")
    print("2. Vectores c=(4, -2, 4) y d=(3, -6, -2)")
    print("3. Ingresar vectores manualmente")
    choice = input("Elige una opción (1-3): ")

    if choice == '1':
        a = np.array([3, 2, -6])
        b = np.array([4, -3, 1])
    elif choice == '2':
        a = np.array([4, -2, 4])
        b = np.array([3, -6, -2])
    elif choice == '3':
        a = np.array([float(input("Ingresa las coordenadas de a (x, y, z): ")), 
                      float(input()), 
                      float(input())])
        b = np.array([float(input("Ingresa las coordenadas de b (x, y, z): ")), 
                      float(input()), 
                      float(input())])
    else:
        print("Opción inválida.")
        return

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
    ax.quiver(*origin, *a, color='r', label='Vector a')
    ax.quiver(*origin, *b, color='b', label='Vector b')

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

# Menu
def menu():
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Calcular campo escalar")
        print("2. Calcular derivadas parciales")
        print("3. Calcular área de un triángulo")
        print("4. Calcular ángulo entre dos vectores")
        print("5. Salir")

        choice = input("Elige una opción (1-5): ")

        if choice == '1':
            campo_escalar()
        elif choice == '2':
            derivadas_parciales()
        elif choice == '3':
            area_triangulo()
        elif choice == '4':
            angulo_vectores()
        elif choice == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()

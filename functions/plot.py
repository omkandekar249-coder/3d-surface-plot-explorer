import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_surface(X, Y, Z):
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title("3D Surface Plot")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("f(x, y)")

    fig.colorbar(surf, shrink=0.5, aspect=10)
    plt.show()

def plot_contour(X, Y, Z):
    plt.figure(figsize=(8, 6))
    plt.contourf(X, Y, Z, levels=30, cmap='viridis')
    plt.title("Contour Map")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.colorbar()
    plt.show()

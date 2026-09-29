import numpy as np

def generate_surface(f, x_range, y_range, density=50):
    x = np.linspace(*x_range, density)
    y = np.linspace(*y_range, density)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    return X, Y, Z

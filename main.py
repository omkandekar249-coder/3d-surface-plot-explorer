import numpy as np
from functions.parser import parse_function
from functions.surface import generate_surface
from functions.plot import plot_surface, plot_contour

print("3D Surface Plot Explorer")

user_input = input("Enter a function f(x, y): ")

f = parse_function(user_input)

xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
ymin = float(input("Enter ymin: "))
ymax = float(input("Enter ymax: "))

density = int(input("Enter density (40–80 recommended): "))

X, Y, Z = generate_surface(f, (xmin, xmax), (ymin, ymax), density)

plot_surface(X, Y, Z)
plot_contour(X, Y, Z)


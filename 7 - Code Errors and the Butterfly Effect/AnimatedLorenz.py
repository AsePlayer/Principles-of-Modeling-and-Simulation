"""
Project 7: Code Errors and the Butterfly Effect Part 1
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


def lorenz(x, y, z, r, s=10, b=2.667):  # calculates Lorenz equation
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return x_dot, y_dot, z_dot


dt = 0.01  # change in time

# Empty Arrays for points
xs = []
ys = []
zs = []

# Set initial values for points
xs.append(.248)
ys.append(1.357)
zs.append(1.884)


def animate(i):  # appends each new point to the arrays and plots the new changes
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i], r)
    xs.append((xs[i] + (x_dot * dt)))
    ys.append((ys[i] + (y_dot * dt)))
    zs.append((zs[i] + (z_dot * dt)))
    plt.cla()
    plt.plot(xs, ys, zs)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')  # creates a 3d graph
r = int(input("What r value would you like to graph: "))  # can change R value for variety
animation = FuncAnimation(fig, animate, interval=0, blit=False)  # animates the graph

plt.show()


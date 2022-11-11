"""
Project 5: Self-Organized Criticality
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import numpy as np
import matplotlib.pyplot as plt


dt = 0.01   # Step size
num_steps = 10001   # Steps
xs, ys, zs = np.empty(num_steps), np.empty(num_steps), np.empty(num_steps)  # Creates empty space
xs[0], ys[0], zs[0] = (.69, .420, .1337)   # NICE initial conditions!


def Lorenz(x, y, z, r, s=10, b=2.667):
    x_dot = (y - x) * s             # Calculates dx/dt
    y_dot = (r * x) - y - (x * z)   # Calculates dy/dt
    z_dot = (x * y) - (b * z)       # Calculates dz/dt

    return (x_dot, y_dot, z_dot)


def plotGraphs(plot_x, plot_y, plot_z, lin, r):
    fig = plt.figure()  # Displays all graphs in the same window

    graph = fig.add_subplot(2, 2, 1, projection='3d')  # Create 3D graph
    graph.plot(plot_x, plot_y, plot_z, linewidth=0.5)  # Graph X, Y, Z in 3D
    graph.set_xlabel("X Axis")
    graph.set_ylabel("Y Axis")
    graph.set_zlabel("Z Axis")
    graph.set_title("Lorenz")

    graph = fig.add_subplot(2, 2, 2)         # Create 2nd graph
    graph.plot(lin, plot_x, linewidth=0.75)  # Plot time and X values
    graph.set_xlabel("t")
    graph.set_ylabel("x")
    graph.set_title(f"x(t) - r: {r}")

    graph = fig.add_subplot(2, 2, 3)         # Create 3rd graph
    graph.plot(lin, plot_y, linewidth=0.75)  # Plot time and Y values
    graph.set_xlabel("t")
    graph.set_ylabel("y")
    graph.set_title(f"y(t) - r: {r}")

    graph = fig.add_subplot(2, 2, 4)         # Create 4th graph
    graph.plot(lin, plot_z, linewidth=0.75)  # Plot time and Z values
    graph.set_xlabel("t")
    graph.set_ylabel("z")
    graph.set_title(f"z(t) - r: {r}")

    plt.show()


def R_TIME(r):
    for i in range(num_steps - 1):
        x_dot, y_dot, z_dot = Lorenz(xs[i], ys[i], zs[i], r)
        xs[i + 1] = xs[i] + (x_dot * dt)
        ys[i + 1] = ys[i] + (y_dot * dt)
        zs[i + 1] = zs[i] + (z_dot * dt)

    lin = np.linspace(0, 100, num=10001)
    plotGraphs(xs, ys, zs, lin, r)


# Test values
R_TIME(1)   # Normal
R_TIME(10)  # Entropy
R_TIME(20)  # Insanity!

# Try your own values!
while True:
    R_TIME(int(input("Enter an R value: ")))

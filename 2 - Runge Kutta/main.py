# Ryan Scott
# CST-305
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt


# Initial Conditions
x0 = 1
y0 = 5
h = .02

# Arrays for storing values
xPoints = [x0]
yPoints = [y0]


# Equation
def ODEmodel(y,x):
    return y / (np.e ** x - 1)


def RKmodel(x,y):
    return y / (np.e ** x - 1)


# Calculates k1-k4 for RK
def RungeKuttaAlgorithm(x0,y0,h):
    k1 = RKmodel(x0, y0)
    k2 = RKmodel(x0 + (h / 2), y0 + ((h / 2) * k1))
    k3 = RKmodel(x0 + (h / 2), y0 + ((h / 2) * k2))
    k4 = RKmodel(x0 + h, y0 + (h * k3))

    # Calculating the y(n+1)th value
    y1 = y0 + (h / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
    # Increment step size
    x1 = x0 + h

    # Prints & returns x(n+1), y(n+1) coordinate pair
    print("Point (x(n+1), y(n+1)) =", (x1, y1))
    return((x1, y1))


# Uses Runge-Kutta algorithm to calculate 1000 points
for i in range(1000):
    print(f"\t#{i+1}\t".format(i))

    # Recursively solves the RK algorithm
    x0, y0 = RungeKuttaAlgorithm(x0, y0, h)

    xPoints.append(x0)
    yPoints.append(y0)


# Uses odeint to calculate 1000 points
y0 = 5
ODE = odeint(ODEmodel, y0, xPoints)


# Plotting

# Runge-Kutta Graph
plt.plot(xPoints, yPoints, color='crimson', linestyle='dashed', linewidth= 1)
plt.suptitle("1,000 Points Runge-Kutta Algorithm for y/e^x-1")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# ODE graph
plt.plot(xPoints, ODE, 'cornflowerblue', linewidth=1)
plt.suptitle("1,000 Points ODE for y/e^x-1")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#Both RK and ODE graph
plt.plot(xPoints, ODE, 'cornflowerblue', linewidth=2, label="ODE")
plt.plot(xPoints, yPoints, 'crimson', linewidth=1, linestyle='dashed', label="Runge-Kutta")
plt.suptitle("1,000 Points Comparison of Runge-Kutta and ODE for y/e^x-1")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
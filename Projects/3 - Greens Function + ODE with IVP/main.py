"""
Project 3: Green's Function and ODE with IVP
Diego Guerra & Ryan Scott
CST-305
Dr. Ricardo Citro
"""

# Imports
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import time


# ODEs
# V is a vector where V[0] = y and V[1] = y'
def ODE1(V, x):  # returns y' and -2y' - y + 2x
    return [V[1], -2 * V[1] - V[0] + 2 * x]


def ODE2(V, x):  # returns y' and x^2 - y
    return [V[1], x ** 2 - V[0]]


# Green's formulas
def greens1(x):  # returns the function of y(x) = 4e^(-x) + 2xe^(-x) + 2x - 4
    return (4 * np.exp(-x) + 2 * x * np.exp(-x) + 2 * x - 4)


def greens2(x):  # returns the function of y(x) = x^2 + 2 * cos(x) - 2
    return (x ** 2 + 2 * np.cos(x) - 2)


# Initialize Time Analysis Variables
timeStart0 = timeEnd0 = 0  # time start and end for 1st analysis
timeStart1 = timeEnd1 = 0  # time start and end for 2nd analysis
timeStart2 = timeEnd2 = 0  # time start and end for 3rd analysis
timeStart3 = timeEnd3 = 0  # time start and end for 4th analysis

##### Odeint Solution 1 #######################################
timeStart0 = time.time()

V0 = [0, 0]  # contains the values of y and y'
x0_space = np.linspace(0, 20, 1000)  # x space from 0-20 with 1000 steps
y0_space = odeint(ODE1, V0, x0_space)  # y space using Odeint
y0_space = y0_space[:, 0]  # cleaning up unused y space data

timeEnd0 = time.time()
print("Odeint 1 analysis: " + str(timeEnd0 - timeStart0) + " seconds!")

##### Odeint Solution 2 #######################################
timeStart1 = time.time()

V1 = [0, 0]  # contains the values of y and y'
x1_space = np.linspace(0, 20, 1000)  # x space from 0-20 with 1000 steps
y1_space = odeint(ODE2, V1, x1_space)  # y space using Odeint
y1_space = y1_space[:, 0]  # cleaning up unused y space data

timeEnd1 = time.time()
print("Odeint 2 analysis: " + str(timeEnd1 - timeStart1) + " seconds!")

# Initialize Green's Formula variables
n = 1000  # initial n value of 1000 chosen
h = 0.02  # initial h value of 0.02 as outlined in the assignment

x0 = x1 = y0 = y1 = 0  # hold variables

x2_space = []  # x2 space for Green's function
y2_space = []  # y2 space for Green's function
x3_space = []  # x3 space for Green's function
y3_space = []  # y3 space for Green's function

##### Green's Formula Solution 1 ##############################
timeStart2 = time.time()

for i in range(n):  # for loop to run the green function function 1000 times
    x2_space.append(x0)  # append x-value to x-space
    y2_space.append(y0)  # append y-value to y-space
    y0 = greens1(x0)  # get new updated y-value using the Green's Function
    x0 += h  # increment step
timeEnd2 = time.time()
print("Green's Function 1 analysis: " + str(timeEnd2 - timeStart2) + " seconds!")

##### Green's Formula Solution 2 ##############################
timeStart3 = time.time()

for i in range(n):  # for loop to run the green function function 1000 times
    x3_space.append(x1)  # append x-value to x-space
    y3_space.append(y1)  # append y-value to y-space
    y1 = greens2(x1)  # get new updated y-value using the Green's Function
    x1 += h  # increment step

timeEnd3 = time.time()
print("Green's Function 2 analysis: " + str(timeEnd3 - timeStart3) + " seconds!")

plt.style.use("ggplot")

##### Function 1 Graphing #######################################
plt.title("Function 1:\n ODE Function Analysis")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x0_space, y0_space, color="cornflowerblue", linestyle="solid", label="Odeint 1", linewidth=2)
plt.legend()
plt.show()

plt.title("Function 1:\n Green's Function Analysis")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x2_space, y2_space, color="red", linestyle="dotted", label="Green's Function 1", linewidth=2)
plt.legend()
plt.show()

plt.title("Function 1:\n ODE and Green's Function Analysis")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x0_space, y0_space, color="cornflowerblue", linestyle="solid", label="Odeint 1", linewidth=2)
plt.plot(x2_space, y2_space, color="red", linestyle="dotted", label="Green's Function 1", linewidth=2)
plt.legend()
plt.show()

##### Function 2 Graphing #######################################
plt.title("Function 2:\n ODE Function Analysis")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x1_space, y1_space, color="cornflowerblue", linestyle="solid", label="Odeint 2", linewidth=2)
plt.legend()
plt.show()

plt.title("Function 2:\n Green's Function Analysis")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x3_space, y3_space, color="red", linestyle="dotted", label="Green's Function 2", linewidth=2)
plt.legend()
plt.show()

plt.title("Function 2:\n ODE and Green's Function Analysis")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x1_space, y1_space, color="cornflowerblue", linestyle="solid", label="Odeint 2", linewidth=2)
plt.plot(x3_space, y3_space, color="red", linestyle="dotted", label="Green's Function 2", linewidth=2)
plt.legend()
plt.show()
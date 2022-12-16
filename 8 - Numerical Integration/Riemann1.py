"""
Project 8: Numerical Integration
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import numpy as np
import matplotlib.pyplot as plt
import math


# f(x) = sin(x) + 1
def func(x):
    return math.sin(x) + 1


r = 100     # Number of points
interval = np.linspace(-math.pi, math.pi, r)  # Start conditions

# Gets y values for the sine graph
y = []
for i in range(0, len(interval)):
    y.append(func(interval[i]))

# Get variables for Riemann Sum
start = -math.pi
end = math.pi
subintervals = 4
result = (end - start) / subintervals
low = min(y)
high = max(y)

# Gets rectangles for Riemann Sum
x_left = []
y_left = []
index = start
for i in range(0, subintervals):
    x_left.append(index)
    y_left.append(func(index))
    index += result

x_center = []
y_center = []
index = start + result / 2
for i in range(0, subintervals):
    x_center.append(index)
    y_center.append(func(index))
    index += result

x_right = []
y_right = []
index = start + result
for i in range(0, subintervals):
    x_right.append(index)
    y_right.append(func(index))
    index += result

# Display plots (left)
fig, ax1 = plt.subplots()
ax1.plot(interval, y)
ax1.set_ylabel('y')
ax1.set_ylim(low, high)

ax2 = ax1.twinx()
ax2.bar(x_left, y_left, width=result, align='edge', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(low, high)

plt.show()

# Calculates sum
l_sum = 0
for i in y_left:
    l_sum += i * result

print("Left Riemann Sum: ", l_sum)
print(y_left)

# Display plots (center)
fig, ax1 = plt.subplots()
ax1.plot(interval, y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_ylim(low, high)

ax2 = ax1.twinx()
ax2.bar(x_center, y_center, width=result, align='center', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(low, high)

plt.show()

# Calculates sum
c_sum = 0
for i in y_center:
    c_sum += i * result

print("Center Riemann Sum: ", c_sum)
print(y_center)

# Display plots (right)
fig, ax1 = plt.subplots()
ax1.plot(interval, y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_ylim(low, high)

ax2 = ax1.twinx()
ax2.bar(x_right, y_right, width=-result, align='edge', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(low, high)

plt.show()

# Calculates sum
r_sum = 0
for i in y_right:
    r_sum += i * result

print("Right Riemann Sum: ", r_sum)
print(y_right)

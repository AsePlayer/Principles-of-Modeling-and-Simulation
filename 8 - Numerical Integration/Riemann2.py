"""
Project 8: Numerical Integration
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import numpy as np
import matplotlib.pyplot as plt
import math


# f(x) = ln(x)
def func(x):
    return math.log(x)


# Get variables for Riemann Sum
start = 1
end = math.e
subintervals = 4000
result = (end - start) / subintervals

r = 100     # Number of points
domain = np.linspace(start, end, r)     # Start conditions

# Gets y values for the graph
y = []
for i in range(0, len(domain)):
    y.append(func(domain[i]))

# Finds y range
low = min(y)
high = max(y)

# Gets rectangles for Riemann Sum
x_center = []
y_center = []
index = start + result / 2
for i in range(0, subintervals):
    x_center.append(index)
    y_center.append(func(index))
    index += result

# Display plots (center)
fig, ax1 = plt.subplots()
ax1.plot(domain, y)
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
print("Granularity: ", subintervals)

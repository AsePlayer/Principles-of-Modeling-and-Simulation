"""
Project 8: Numerical Integration
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Get variables for Riemann Sum
start = 0
end = 30
subintervals = 30
interval = (end - start) / subintervals

# Start conditions
domain = np.linspace(0, 30, 31)

# Gets y values for the graph
y = [17.0, 17.3, 19.4, 15.8, 20.2, 16.5,
     23.7, 19.9, 21.1, 20.9, 19.1, 20.4,
     18.0, 17.5, 21.4, 18.7, 19.8, 18.5,
     15.5, 22.4, 18.5, 17.9, 16.8, 16.4,
     15.9, 21.8, 15.8, 18.7, 21.2, 17.1,
     16.5]

for i in range(0, len(y)):
    y[i] *= 60

# Finds y range
low = min(y)
high = max(y)

# Display plots (center)
fig, ax1 = plt.subplots()
ax1.plot(domain, y)
ax1.set_ylabel('MB/min')
ax1.set_xlabel('minute')
ax1.set_ylim(0, high)

# Set bar graph
y.pop()
domain = np.linspace(0, 29, 30)

ax2 = ax1.twinx()
ax2.bar(domain, y, width=interval, align='edge', alpha=0.5, color='red')
ax2.grid(False)
ax2.set_ylim(0, high)

plt.show()

# Calculates sum
c_sum = 0
for i in y:
    c_sum += i * interval

print("Left Riemann Sum: ", c_sum)
print("Granularity: ", subintervals)

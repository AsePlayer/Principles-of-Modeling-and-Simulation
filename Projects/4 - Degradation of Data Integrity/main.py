"""
Project 4: Degradation of Data Integrity
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# Our functions
def xt1(x):
    return np.exp(-.05 * x)

def xt2(x):
    return -np.exp(-.05 * x)

# Record start time
start = time.time()

# Number of points
r = 101

# Start conditions
x1 = np.linspace(0, r - 1, r)
x2 = np.linspace(0, r - 1, r)

# Calculates Processor A & B
y1 = xt1(x1)
y2 = xt2(x2)

# Calculates program's runtime
print(f"Operation took {time.time() - start} seconds.")

# Plot A and B together
plt.plot(x1, y1, label='A', color='red')
plt.plot(x2, y2, label='B', color='green')
plt.xlabel('time')
plt.ylabel('data')
plt.legend()
plt.show(block=False)

# Search the list for values
while (True):
    index = int(input("Enter an integer 0 - 100: "))
    print(f"Processor A: x({index}) = {x1[int(index)]}, y({index})  = {y1[int(index)]}")
    print(f"Processor B: x({index}) = {x2[int(index)]}, y({index})  = {y2[int(index)]}")
  
'''
Programmed By: Ryan Scott
Packages Used: matplotlib, numpy, scipy
The approach for implementation of this program was inspired from the slides on Padlet.
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dx/dt
def model(x,t):
    k = 0.4
    # Data rate in bps = k * log_2(x)
    dxdt = -k * (np.log(2) * x)
    return dxdt

# initial condition
x0 = -5

# time points
t = np.linspace(0,20)

# solve ODE
x = odeint(model,x0,t)

# plot results
plt.plot(t,x,linestyle="--",label='k = 0.4')

plt.xlabel('time (seconds)')
plt.ylabel('bits (x/t)')
plt.legend()
plt.show()
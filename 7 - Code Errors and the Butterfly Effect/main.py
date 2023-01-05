"""
Project 7: Code Errors and the Butterfly Effect Part 2
Ryan Scott & Diego Guerra
CST-305
Dr. Ricardo Citro
"""

import matplotlib.pyplot as plt
import numpy as np

arrivalTime = np.linspace(1, 15, 15)  # X domain for all of the graphs
serviceDuration = [2.22, 1.76, 2.13, .14, .76, .7, .47, .22, .18, 2.41, .41, .46, 1.37, .27,
                   .27]  # Array of service duration values

# Customer arrival time as a function of service start time
serviceStartTime = [1, 3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 10, 12.41, 12.82, 13.28, 14.65, 15]

# Customer arrival time as a function of exit time
serviceExitTime = [3.22, 4.98, 7.11, 7.25, 8.01, 8.71, 9.18, 9.4, 9.58, 12.41, 12.82, 13.28, 14.65, 14.92, 15.27]

# Customer arrival time as a function of time in queue
timeInQueue = [0, 1.22, 1.98, 3.11, 2.25, 2.01, 1.71, 1.18, 0.48, 0, 1.41, 0.82, 0.28, 0.65, 0]

# Customer arrival time as a function of the number of customers in system
customersInSystem = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]

# Customer arrival time as a function of number of customers in queue
customersInQueue = [0, 1, 2, 2, 2, 3, 4, 3, 2, 0, 1, 2, 1, 1, 0]

# ----------------------------------------------------------------------------------------------------------

fig, ax = plt.subplots(2, 3)  # Creates 6 graphs in one tab to be fancy
fig.tight_layout()

# Plots and labels arrival time vs. service start time
ax[0, 0].plot(arrivalTime, serviceStartTime)
ax[0, 0].set_title("Arrival Time vs. Service Start Time")
ax[0, 0].set_xlabel("Arrival Time")
ax[0, 0].set_ylabel("Start Time")

# Plots and labels arrival time vs. service exit time
ax[0, 1].plot(arrivalTime, serviceExitTime)
ax[0, 1].set_title("Arrival Time vs. Exit Time")
ax[0, 1].set_xlabel("Arrival Time")
ax[0, 1].set_ylabel("Exit Time")

# Plots and labels arrival time vs. time in queue
ax[1, 0].plot(arrivalTime, timeInQueue)
ax[1, 0].set_title("Arrival Time vs. Time in Queue")
ax[1, 0].set_xlabel("Arrival Time")
ax[1, 0].set_ylabel("Time in Queue")

# Plots and labels arrival time vs. customers in system
ax[1, 1].plot(arrivalTime, customersInSystem)
ax[1, 1].set_title("Arrival Time vs. # of Customers in System")
ax[1, 1].set_xlabel("Arrival Time")
ax[1, 1].set_ylabel("# of Customers in System")

# Plots and labels arrival time vs. customers in queue
ax[0, 2].plot(arrivalTime, customersInQueue)
ax[0, 2].set_title("Arrival Time vs. # of Customers in Queue")
ax[0, 2].set_xlabel("Arrival Time")
ax[0, 2].set_ylabel("# of Customers in Queue")

# Unused graph, only need 5/6 but the display is 2x3
ax[1, 2].plot()
ax[1, 2].set_title("Blank Graph")
ax[1, 2].set_xlabel("Blank")
ax[1, 2].set_ylabel("Blank")

plt.show()


# ----------------------------------------------------------------------------------- #
old_mu = 500  # Value found in part 2b
old_lambda = 125  # Value found in part 2b

k = np.linspace(1, 1000, 1001)  # creates k domain from 1-1000

# 6 equations found by hand and put into Python
new_mu = k * old_mu
new_lambda = k * old_lambda
new_rho = new_lambda / new_mu
new_x = new_lambda
new_EN = new_rho / (1 - new_rho)
new_ET = 1 / (new_mu - new_lambda)

fig, ax = plt.subplots(2, 3)  # plotting the equations as a form of k vs. equation
fig.tight_layout()

ax[0, 0].plot(k, new_lambda)
ax[0, 0].set_title("k vs. New Lambda")
ax[0, 0].set_xlabel("k")
ax[0, 0].set_ylabel("New Lambda")

ax[0, 1].plot(k, new_mu)
ax[0, 1].set_title("k vs. New Mu")
ax[0, 1].set_xlabel("k")
ax[0, 1].set_ylabel("New Mu")

ax[1, 0].plot(k, new_rho)
ax[1, 0].set_title("k vs. New Rho")
ax[1, 0].set_xlabel("k")
ax[1, 0].set_ylabel("New Rho")

ax[1, 1].plot(k, new_x)
ax[1, 1].set_title("k vs. New x")
ax[1, 1].set_xlabel("k")
ax[1, 1].set_ylabel("New x")

ax[0, 2].plot(k, new_EN)
ax[0, 2].set_title("k vs New E[N]")
ax[0, 2].set_xlabel("k")
ax[0, 2].set_ylabel("New E[N]")

ax[1, 2].plot(k, new_ET)
ax[1, 2].set_title("k vs. New E[T]")
ax[1, 2].set_xlabel("k")
ax[1, 2].set_ylabel("New E[T]")

plt.show()


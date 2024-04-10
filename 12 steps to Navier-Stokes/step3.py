import numpy as np
from matplotlib import pyplot
import time, sys

# 2nd degree diffusion problem

# setup
nx = 41 # number of nodes
dx = 2/(nx -1) # distance between nodes
nt = 25 # number time steps
nu = 0.3 # viscocity
sigma = 0.2
dt = sigma * dx**2 /nu # time step

#initial condition
u = np.ones(nx) # u=1 everywhere
u[int(0.5/dx):int(1/dx+1)] = 2 # u=2 for between x 0.5 and 1
print(u)
pyplot.plot(np.linspace(0,2,nx),u)

# solving
un = np.ones(nx)
for n in range(nt):
    un = u.copy()
    for i in range(nx):
        u[i] = un[i] - nu * dt / dx**2 * (un[i] - un[i-1])

pyplot.plot(np.linspace(0, 2, nx), u)

pyplot.show()
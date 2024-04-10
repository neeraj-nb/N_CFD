import numpy as np
from matplotlib import pyplot
import time, sys

# 1D non linear diffusion problem

# setup
nx = 41 # number of nodes
dx = 2/(nx -1) # distance between nodes
nt = 2500 # number time steps
dt = 0.00025 # time step
c = 1 # wave speed

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
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i-1])

pyplot.plot(np.linspace(0, 2, nx), u);

pyplot.show()
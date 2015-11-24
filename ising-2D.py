#!/usr/bin/env python

from math import *
import numpy as np
import random
import matplotlib.pyplot as plt

## Some initial values
#kT = 2.0/log(1.0+sqrt(2.0))
kT = 1.0
size = 100
J = -1.0
t = 5000000

## Initialize the grid and the spins randomly
grid = np.empty((size, size))
for j in range(size):
    for i in range(size):
        if (np.random.uniform() > 0.5):
            grid[i][j] = 1
        else:
            grid[i][j] = -1
            
## Plot the original grid
figOrigin = plt.figure()
plotOrigin = plt.subplot(111)
plotOrigin.pcolor(grid, cmap="Reds")
            
## Run the Monte Carlo algorithm t times
for d in range(t):
    ## Look at a random spin
    i = int(np.random.uniform() * size)
    j = int(np.random.uniform() * size)
    ## Compute the change of energy of flipping it
    deltaE = 2.0*J*grid[i][j]*(grid[(i-1)%size][j] + grid[(i+1)%size][j] + grid[i][(j-1)%size] + grid[i][(j+1)%size])
    ## Transition probability
    p = exp(-deltaE / kT)
    ## Should the transition happen?
    if (np.random.uniform() <= p):
        ## Switch the spin
        grid[i][j] = -1 * grid[i][j]
   
## Plot the final grid
figFinal = plt.figure()
plotFinal = plt.subplot(111)
plotFinal.pcolor(grid, cmap="Reds")

## Compute the magnetization
M = 0
for j in range(size):
    for i in range(size):
        M = M + grid[i][j]

## Rescale M
M = M / float(size*size)
        
print 'M = ', M

## Show the plots
plt.show()
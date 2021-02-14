# following example in FDTD PDF page 6
import numpy as np
import matplotlib.pyplot as plt
import time

def e_field(time_steps, grid_size):
    c = 3e8

    # number of space points
    ke = grid_size

    # position of source
    ks = int(ke/2)

    # number of time steps
    nsteps= time_steps # 100

    # space and time discretization
    dx = 0.01
    dt = dx/(2*c)
    cc = c*dt/dx

    # E H
    ex = np.zeros(ke)
    hy = np.zeros(ke)

    # Gaussian Pulse
    t0 = 20
    spread = 8

    for t in range(nsteps):
        for k in range(1, ke-1):
            ex[k] = ex[k] + cc * ( hy[k-1] - hy[k] )

        ex[ks] = np.exp(-0.5*((t-t0)/spread)**2)

        for k in range(1, ke-1):
            hy[k] = hy[k] + cc * ( ex[k] - ex[k+1] )

    return ex

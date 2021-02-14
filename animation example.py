# https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from Air_1D import e_field
plt.style.use('seaborn-pastel')


fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,
def animate(i):
    print(i)
    grid_size = 100
    line.set_data(range(grid_size), e_field(i, grid_size))
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=300, interval=20, blit=True)


anim.save('gaussian_pulse_in_air.gif', writer='imagemagick')
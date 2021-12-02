import numpy as np
import matplotlib.pyplot as plt
from rational_package import *
from matplotlib.animation import FuncAnimation



def graph(lst):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    x = np.linspace(-10, 10)

    for q in lst:
        if not is_infinity(q):
            m = float_rep(q)
            ax.plot(x, m * x, linewidth = 1 / m)
    
    plt.show()
     
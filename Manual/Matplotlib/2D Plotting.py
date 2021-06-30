import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

x = np.linspace(0, 2*np.pi, 30)
y = np.sin(x)

fig = plt.figure(num=1)
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='minor', width=0.5, length=3)
ax.tick_params(which='both', top=True, right=True, labeltop=True, labelright=True)
ax.grid(which='major', linestyle='--')
ax.grid(which='minor', linestyle='dotted')
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_aspect('equal', adjustable='box')

ax.plot(x, y, marker='.', linestyle='-', color='royalblue', label="sinusoid")
ax.set_xlim(-.2, 2*np.pi + 0.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.text(0, 0, r"$\mu$")
ax.annotate("local max", xy=(np.pi/2, 1), xytext=(np.pi/2 + .2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05)
            )
ax.legend()

plt.show()

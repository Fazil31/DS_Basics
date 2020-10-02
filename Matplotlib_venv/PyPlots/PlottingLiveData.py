from itertools import count
import random
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(self):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))

    plt.cla() # clear axis
    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

plt.tight_layout()
plt.show()


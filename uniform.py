import numpy as np
from plot_utils import my_plot

size = 1000
x = np.linspace(0, size, size)
y = np.random.uniform(0, 1, size)
my_plot(x, y)
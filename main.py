import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import copy
from MyLib import *

# Setting up the plotting
xmin = -2
xmax = 2
x = np.linspace(xmin, xmax)
y = copy.deepcopy(x)
X, Y = np.meshgrid(x, y)
Z = MyFun(X, Y)

# Generating the data which we will fit the new function against
data_set = SampleData(X, Y, Z, 10)

# c here will ultimately be what the genetic algorithm will optimize
c = np.random.randn(6)
Z_approx = GeneralFunction(c, X, Y)

# Setting up the plot for the target surface and the approximation surface
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1 = f.add_subplot(1, 2, 1, projection='3d')
Z_error = Z - Z_approx
surf1 = ax1.plot_surface(X, Y, Z_approx)
surf2 = ax1.plot_surface(X, Y, Z)
# Plotting the generated data
scatter = ax1.scatter(data_set['x'], data_set['y'], data_set['z'], c='r')

# An attempt to visualise the error
ax2 = f.add_subplot(1, 2, 2)
plt.pcolormesh(X, Y, -np.abs(Z_error), cmap = cm.RdYlGn)
plt.show()

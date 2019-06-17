import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy
from MyLib import *

xmin = -2
xmax = 2

x = np.linspace(xmin, xmax)
y = copy.deepcopy(x)

X, Y = np.meshgrid(x, y)
Z = MyFun(X, Y)

data_set = SampleData(X, Y, Z, 10)


fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z)
scatter = ax.scatter(data_set['x'], data_set['y'], data_set['z'], c='r')
plt.show()

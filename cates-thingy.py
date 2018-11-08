from random import randint
import numpy as np
import matplotlib.pyplot as plt

points = input('Enter number of points to plot: ')


#I miss err != nil
N = int(points)
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y)
plt.show()




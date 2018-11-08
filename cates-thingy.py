from random import randint
import numpy as np
import matplotlib.pyplot as plt


def genRandomNumber(a,b):
     return randint(a, b)

def genRandomArray(a, b):
    i = 0
    array = []
    while i < 300:
        array.append(genRandomNumber(a,b))
        i = i + 1
    return array
a = genRandomArray(0,10)


N =  1
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y)
plt.show()




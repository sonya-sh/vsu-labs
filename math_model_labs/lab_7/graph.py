import matplotlib.pyplot as plt
import numpy as np


def fun(x):
    return x * np.sin(1/x)


a = float(input('Введите а: '))
b = float(input('Введите b: '))

x1 = np.arange(a, b, 0.0001)
plt.plot(x1, fun(x1))
plt.show()

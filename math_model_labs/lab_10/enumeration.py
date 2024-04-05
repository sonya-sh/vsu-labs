import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

x0 = np.array([1, 1])
x11 = 0
x12 = 6
x21 = 0
x22 = 3
eps = 0.01


def fun(x):
    return (4 - x[0])**2 + (x[0] - x[1]**2)**2


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

X, Y = np.meshgrid(np.linspace(0, 6, 1000), np.linspace(0, 3, 1000))
Z = fun(np.array([X, Y]))

ax.plot_surface(X, Y, Z)


def enumeration(x11, x12, x21, x22, eps):
    accuracy = abs(len(str(eps))) - 1
    x = [[x11, x21]]
    n = 10**accuracy
    k = 0
    for i in range(n):
        x11 += x12/n
        x21 += x22/n
        x.append([round(x11, accuracy), round(x21, accuracy)])
    minx = np.array(x[0])
    for i in range(n):
        if fun(np.array(x[i + 1])) <= fun(minx):
            minx = np.array(x[i + 1])
            k += 1
    print("Число итераций: ", k)
    return minx


start = datetime.now()
opt = enumeration(x11, x12, x21, x22, eps)
print('Время выполнения ', datetime.now() - start)
print('X = ', opt)
print('f(X) = ', fun(opt))

ax.scatter(opt[0], opt[1], fun(opt), s=50, color='red')
plt.show()

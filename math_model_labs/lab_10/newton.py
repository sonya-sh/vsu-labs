import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

x0 = np.array([1, 1])
eps = 0.01


def fun(x):
    return (4 - x[0])**2 + (x[0] - x[1]**2)**2


def der(x):
    return np.array([x[0]*4-2*x[1]**2-8, -4*x[0]*x[1]+4*x[1]**3])


def hes(x):
    return np.array([[4, -4*x[1]], [-4*x[1], -4*x[0]+12*x[1]**2]])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

X, Y = np.meshgrid(np.linspace(0, 6, 1000), np.linspace(0, 3, 1000))
Z = fun(np.array([X, Y]))

ax.plot_surface(X, Y, Z)


def newton_method(x0, eps):
    xmin = x0 - np.dot(der(x0), np.linalg.inv(hes(x0)))
    x = x0
    i = 0
    while abs(xmin - x)[0] >= eps or abs(xmin - x)[1] >= eps:
        x = xmin
        xmin = x - np.dot(der(x), np.linalg.inv(hes(x)))
        i += 1
    print("Число итераций: ", i)
    return xmin


start = datetime.now()
opt = newton_method(x0, eps)
print('Время выполнения ', datetime.now() - start)
print("X = ", opt)
print("f(X) = ", fun(opt))

ax.scatter(opt[0], opt[1], fun(opt), s=50, color='red')
plt.show()

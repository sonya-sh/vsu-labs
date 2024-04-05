import math
import matplotlib.pyplot as plt


def fun(x, y):
    return 0.4 * y + 0.6 * x**2 + 1.7


def fun_y(x):
    return 24 * math.e**(0.4*x) - 1.5*x**2 - 7.5*x - 23


def RK4(h, x, y, fun, acc):
    td = []
    tx = ['xi', 0]
    ty = ['yi Runge-Kutta', 1]
    ty_y = ['yi точное', 1]
    x = round(float(x), 1)
    y = float(y)
    n = int(2 / h)
    ti = ['i', 0]
    for i in range(n):
        ti.append(i + 1)
        k1 = fun(x, y)
        x = x + 0.5 * h
        k2 = fun(x, y + 0.5 * k1 * h)
        k3 = fun(x, y + 0.5 * k2 * h)
        x = x + 0.5 * h
        k4 = fun(x, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        tx.append(x)
        ty.append(round(y, acc))
        ty_y.append(round(fun_y(x), acc))
    td.append(ti)
    td.append(tx)
    td.append(ty)
    td.append(ty_y)
    return td


acc = 6
x1 = (RK4(0.2, 0, 1, fun, acc))[1]
x1.remove('xi')
y1 = (RK4(0.2, 0, 1, fun, acc))[2]
y1.remove('yi Runge-Kutta')
y2 = (RK4(0.2, 0, 1, fun, acc))[3]
y2.remove('yi точное')
plt.plot(x1, y1, label='Runge-Kutta4')
plt.plot(x1, y2, label='exact')
plt.legend()
plt.show()

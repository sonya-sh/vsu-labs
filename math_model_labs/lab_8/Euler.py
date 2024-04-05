import math
import matplotlib.pyplot as plt


def fun(x, y):
    return 0.4 * y + 0.6 * x**2 + 1.7


def fun_y(x):
    return 24 * math.e**(0.4*x) - 1.5*x**2 - 7.5*x - 23


def Euler(h, x, y, fun, acc):
    td = []
    tx = ['xi', 0]
    ty = ['yi Euler', 1]
    ty_y = ['yi точное', 1]
    x = round(float(x), 1)
    n = int(2 / h)
    ti = ['i', 0]
    for i in range(n):
        ti.append(i + 1)
        x += h
        x = round(float(x), 1)
        y += h * fun(x, y)
        tx.append(x)
        ty.append(round(y, acc))
        ty_y.append(round(fun_y(x), acc))
    td.append(ti)
    td.append(tx)
    td.append(ty)
    td.append(ty_y)
    return td


acc = 6
x1 = (Euler(0.2, 0, 1, fun, acc))[1]
x1.remove('xi')
y1 = (Euler(0.2, 0, 1, fun, acc))[2]
y1.remove('yi Euler')
y2 = (Euler(0.2, 0, 1, fun, acc))[3]
y2.remove('yi точное')
plt.plot(x1, y1, label='Euler')
plt.plot(x1, y2, label='exact')
plt.legend()
plt.show()

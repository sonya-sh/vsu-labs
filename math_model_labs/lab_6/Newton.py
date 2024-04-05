import matplotlib.pyplot as plt
import numpy as np
from accuracy import find_accuracy


def fun(a, b, x):
    return np.log(x + a) - b * x**2


# x_an = 0.47601
x_an = -0.35315


def fi(a, b, x):
    return x - (np.log(x + a) - b * x**2) * 0.2


def derivative_fun(a, b, x):
    return 1 / (x + a) - 2 * b * x


def newton_method(x0, N, a, b, eps, accuracy):
    x1 = x0 - (fun(a, b, x0) / derivative_fun(a, b, x0))
    x = x0
    i = 0
    while abs(x1 - x) >= eps:
        if i == N:
            y = fun(a, b, x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        x = x1
        x1 = x - (fun(a, b, x) / derivative_fun(a, b, x))
        i += 1
    print("Число итераций: ", i)
    print("X: ", round(x1, accuracy))
    print("Достигнута заданная точность ", eps)
    y = fun(a, b, x1)
    plt.scatter(x1, y, color="red")

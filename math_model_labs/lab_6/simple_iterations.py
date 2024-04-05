import numpy as np
import matplotlib.pyplot as plt
from accuracy import find_accuracy


def fun(a, b, x):
    return np.log(x + a) - b * x**2


# x_an = 0.47601
x_an = -0.35315


def fi(a, b, x):
    return x - (np.log(x + a) - b * x**2)*0.2


def fi2(a, b, x):
    return x + (np.log(x + a) - b * x**2)*0.2


def iteration_method(x0, eps, accuracy, a, b, N):
    x1 = fi(a, b, x0)
    x = x0
    i = 0
    while abs(x1 - x) >= eps:
        if i >= N:
            y = fun(a, b, x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        x = x1
        x1 = fi(a, b, x)
        i += 1
    print("X: ", round(x1, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = fun(a, b, x1)
    plt.scatter(x1, y, color="red")


def iteration_method2(x0, eps, accuracy, a, b, N):
    x1 = fi2(a, b, x0)
    x = x0
    n = 0
    while abs(x1 - x) >= eps:
        if n == N:
            y = fun(a, b, x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        x = x1
        x1 = fi2(a, b, x)
        n += 1
    print("Число итераций: ", n)
    print("X: ", round(x1, accuracy))
    print("Достигнута заданная точность ", eps)
    y = fun(a, b, x1)
    plt.scatter(x1, y, color="red")

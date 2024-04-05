import matplotlib.pyplot as plt
import numpy as np
from accuracy import find_accuracy


def fun(a, b, x):
    return np.log(x + a) - b * x**2


# x_an = 0.47601
x_an = -0.35315


def dichotomy_method(x0, eps, accuracy, a, b, A, B, N):
    i = 0
    while abs(B - A) >= 2*eps:
        i += 1
        if i == N:
            y = fun(a, b, x0)
            plt.scatter(x0, y, color="red")
            acc = find_accuracy(x_an, x0)
            print('заданное кол-во итераций исчерпано, x = ', round(x0, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        if fun(a, b, x0) == 0:
            break
        if fun(a, b, A) * fun(a, b, x0) < 0:
            B = x0
        elif fun(a, b, B) * fun(a, b, x0) < 0:
            A = x0
        x0 = (B + A) / 2
    print("X: ", round(x0, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = fun(a, b, x0)
    plt.scatter(x0, y, color="red")

import matplotlib.pyplot as plt
import numpy as np
from accuracy import find_accuracy


def fun(a, b, x):
    return np.log(x + a) - b * x**2


# x_an = 0.47601
x_an = -0.353151


def chord_method(x0, N, a, b, eps, accuracy, A, B):
    x = x0
    x1 = A - (B - A) * fun(a, b, A) / (fun(a, b, B) - fun(a, b, A))
    print(x1)
    i = 0
    while np.abs(x - x1) >= eps:
        if i == N:
            y = fun(a, b, x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        tmp = x1
        x1 = x - (x1 - x) * fun(a, b, x) / (fun(a, b, x1) - fun(a, b, x))
        print(x1)
        x = tmp
        i += 1
    print("X: ", round(x1, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = fun(a, b, x1)
    plt.scatter(x1, y, color="red")


def chord_method2(x0, N, a, b, eps, accuracy, A, B):
    x = x0
    x1 = B - (B - A) * fun(a, b, B) / (fun(a, b, B) - fun(a, b, A))
    i = 0
    while np.abs(x - x1) >= eps:
        if i == N:
            y = fun(a, b, x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        tmp = x1
        x1 = x - (x - x1) * fun(a, b, x) / (fun(a, b, x) - fun(a, b, x1))
        x = tmp
        i += 1
    print("X: ", round(x1, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = fun(a, b, x1)
    plt.scatter(x1, y, color="red")

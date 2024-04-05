import matplotlib.pyplot as plt
import numpy as np
from accuracy import find_accuracy


x_an = float(2)

A = 1
B = 2.5


def dichotomy_method(x0, eps, accuracy, A, B, N):
    i = 0
    while abs(B - A) >= eps:
        i += 1
        if i == N:
            y = tst_fun(x0)
            plt.scatter(x0, y, color="red")
            acc = find_accuracy(x_an, float(x0))
            print('заданное кол-во итераций исчерпано, x = ', round(x0, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        if tst_fun(x0) == 0:
            break
        if tst_fun(A) * tst_fun(x0) < 0:
            B = x0
        elif tst_fun(B) * tst_fun(x0) < 0:
            A = x0
        x0 = (B + A) / 2
    print("X: ", round(x0, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = tst_fun(x0)
    plt.scatter(x0, y, color="red")


def chord_method(x0, N, eps, accuracy, A, B):
    x = x0
    x1 = A - (B - A) * tst_fun(A) / (tst_fun(B) - tst_fun(A))
    i = 0
    while np.abs(x - x1) >= eps:
        if i == N:
            y = tst_fun(x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        tmp = x1
        x1 = x - (x1 - x) * tst_fun(x) / (tst_fun(x1) - tst_fun(x))
        x = tmp
        i += 1
    print("X: ", round(x1, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = tst_fun(x1)
    plt.scatter(x1, y, color="red")


def chord_method2(x0, N, eps, accuracy, A, B):
    x = x0
    x1 = B - (B - A) * tst_fun(B) / (tst_fun(B) - tst_fun(A))
    i = 0
    while np.abs(x - x1) >= eps:
        if i == N:
            y = tst_fun(x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        tmp = x1
        x1 = x - (x - x1) * tst_fun(x) / (tst_fun(x) - tst_fun(x1))
        x = tmp
        i += 1
    print("X: ", round(x1, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = tst_fun(x1)
    plt.scatter(x1, y, color="red")


def iteration_method(x0, eps, accuracy, N):
    x1 = tst_fi(x0)
    x = x0
    i = 0
    while abs(x1 - x) >= eps:
        if i == N:
            y = tst_fun(x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        x = x1
        x1 = tst_fi(x)
        i += 1
    print("X: ", round(x1, accuracy))
    print("Число итераций: ", i)
    print("Достигнута заданная точность ", eps)
    y = tst_fun(x1)
    plt.scatter(x1, y, color="red")


def newton_method(x0, N, eps, accuracy):
    x1 = x0 - (tst_fun(x0) / tst_derivative_fun(x0))
    x = x0
    i = 0
    while abs(x1 - x) >= eps:
        if i == N:
            y = tst_fun(x1)
            plt.scatter(x1, y, color="red")
            acc = find_accuracy(x_an, x1)
            print('заданное кол-во итераций исчерпано, x = ', round(x1, acc + 2))
            return print('с точностью {} знаков после запятой'.format(acc))
        x = x1
        x1 = x - (tst_fun(x) / tst_derivative_fun(x))
        i += 1
    print("Число итераций: ", i)
    print("X: ", round(x1, accuracy))
    print("Достигнута заданная точность ", eps)
    y = tst_fun(x1)
    plt.scatter(x1, y, color="red")


def tst_fun(x):
    return x**2 - x - 2


def tst_fi(x):
    return x - 0.4 * (x**2 - x - 2)


def tst_derivative_fun(x):
    return 2 * x - 1


x = np.linspace(A, B, 1000)
y1 = tst_fun(x)
plt.plot(x, y1)
y2 = [0 for x in x]
plt.plot(x, y2)
plt.grid(True)
plt.show()


eps = 0.001
accuracy = abs(len(str(eps))) - 2
n = int(input("Число итераций n: "))

print("\nМЕТОД ДИХОТОМИИ")
x01 = float(input("x0 для метода дихотомии: "))
dichotomy_method(x01, eps, accuracy, A, B, n)
plt.title("Метод дихотомии")
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True)
plt.show()

print("\nМЕТОД ХОРД")
x02 = float(input("x0 для метода хорд: "))
chord_method(x02, n, eps, accuracy, A, B)
plt.title("Метод хорд")
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True)
plt.show()

y3 = tst_fi(x)
y4 = x
print("\nМЕТОД ПРОСТЫХ ИТЕРАЦИЙ")
x03 = float(input("x0 для метода простых итераций: "))
iteration_method(x03, eps, accuracy, n)
plt.title("Метод простых итераций")
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.grid(True)
plt.show()

print("\nМЕТОД НЬЮТОНА")
x04 = float(input("x0 для метода Ньютона: "))
newton_method(x04, n, eps, accuracy)
plt.title("Метод Ньютона")
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True)
plt.show()

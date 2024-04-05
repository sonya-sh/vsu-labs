import matplotlib.pyplot as plt
import numpy as np
from dichotomy import dichotomy_method
from gold import golden_ratio
from fibonacci import fib
from accuracy import find_accuracy


def tst_fun(x):
    return x**2 - x - 2


eps = 0.01
accuracy = abs(len(str(eps))) - 2
a = -1
b = 1

x1 = np.arange(a, b, 0.0001)
plt.plot(x1, tst_fun(x1))
plt.show()

print("\nМЕТОД ДИХОТОМИИ")
x_d, n_d = dichotomy_method(tst_fun, a, b, eps)
print('X =', round(x_d, accuracy))
print('Y =', round(tst_fun(x_d), len(str(eps)) - 1))
print('Кол-во итераций', n_d)
print('Точнось {} достигнута'.format(eps))

print("\nМЕТОД ЗОЛОТОГО СЕЧЕНИЯ")
x_g, n_g = golden_ratio(tst_fun, a, b, eps)
print('X =', round(x_g, accuracy))
print('Y =', round(tst_fun(x_g), len(str(eps)) - 1))
print('Кол-во итераций', n_g)
print('Точнось {} достигнута'.format(eps))


x_an = 0.5
y_an = -2.25
x_an_round = round(x_an, accuracy)
y_an_round = round(y_an, accuracy)

print("\nМЕТОД ФИБОНАЧЧИ")
n = int(input("n = "))
x_f, n_f = fib(tst_fun, a, b, eps, n)
x_f = round(x_f, accuracy)
if x_f != x_an_round:
    acc_x = find_accuracy(x_an, x_f)
    acc_y = find_accuracy(y_an, round(tst_fun(x_f), len(str(eps)) - 2))
    print("Кол-во итераций исчерпано")
    print("Найдено X = {}".format(x_f))
    print("с точностью {} знаков после запятой".format(acc_x))
    print("Найдено Y = {}".format(round(tst_fun(x_f), len(str(eps)) - 2)))
    print("с точностью {} знаков после запятой".format(acc_y))

else:
    print('X =', x_f)
    print('Y =', round(tst_fun(x_f), len(str(eps)) - 1))
    print('Кол-во итераций', n_f)
    print('Точнось {} достигнута'.format(eps))

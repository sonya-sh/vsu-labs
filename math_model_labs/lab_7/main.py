import numpy as np
from dichotomy import dichotomy_method
from gold import golden_ratio
from fibonacci import fib
from accuracy import find_accuracy


def fun(x):
    return x * np.sin(1/x)


a = float(input('Введите а: '))
b = float(input('Введите b: '))
eps = float(input('Введите точность: '))

# a = float(0.15)
# b = float(0.5)
# eps = 0.01
accuracy = abs(len(str(eps))) - 2


print("\nМЕТОД ДИХОТОМИИ")
x_d, n_d = dichotomy_method(fun, a, b, eps)
print('X =', round(x_d, len(str(eps)) - 1))
print('Y =', round(fun(x_d), len(str(eps)) - 1))
print('Кол-во итераций', n_d)
print('Точнось {} достигнута'.format(eps))

print("\nМЕТОД ЗОЛОТОГО СЕЧЕНИЯ")
x_g, n_g = golden_ratio(fun, a, b, eps)
print('X =', round(x_g, len(str(eps)) - 1))
print('Y =', round(fun(x_g), len(str(eps)) - 1))
print('Кол-во итераций', n_g)
print('Точнось {} достигнута'.format(eps))

x_an = x_d
x_an_round = int(x_an * 10**accuracy) / 10**accuracy
y_an = fun(x_an)
Y_an_round = int(y_an * 10**accuracy) / 10**accuracy


print("\nМЕТОД ФИБОНАЧЧИ")
n = int(input("n = "))
x_fib, n_f = fib(fun, a, b, eps, n)
x_f = int(x_fib * 10**accuracy) / 10**accuracy
if x_f != x_an_round:
    acc_x = find_accuracy(x_an, x_f)
    acc_y = find_accuracy(y_an, round(fun(x_f), len(str(eps)) - 2))
    print("Кол-во итераций исчерпано")
    print("Найдено X = {}".format(x_f))
    print("с точностью {} знаков после запятой".format(acc_x))
    print("Найдено Y = {}".format(round(fun(x_f), len(str(eps)) - 2)))
    print("с точностью {} знаков после запятой".format(acc_y))

else:
    print('X =', round(x_fib, len(str(eps)) - 1))
    print('Y =', round(fun(x_f), len(str(eps)) - 1))
    print('Кол-во итераций', n_f)
    print('Точнось {} достигнута'.format(eps))

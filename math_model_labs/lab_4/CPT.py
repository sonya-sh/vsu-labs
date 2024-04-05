from random import random
import math


#  переход от значений произвольного распределения v
#  к соответствующим значениям x стандартного распределения.
def norm(v, m, D, n):
    x = (v - (n / 2)) / (math.sqrt(n / 12))
    X = D * x + m  # нормализация ряда
    return X


def gauss_sample(m, d2):
    D = math.sqrt(d2)
    n = 12
    x = []
    for i in range(10000):
        v = 0
        for j in range(n):
            v += random()  # сумма 12 равномерно распределённых случайных величин
        xi = norm(v, m, D, n)  # X = DE + m
        x.append(xi)
        x = sorted(x)
        interval = [x[0], x[-1]]
    return x, interval

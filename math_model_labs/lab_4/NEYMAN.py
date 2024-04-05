from random import random
import math


# закон распределения Релея
def rayleigh(xl, sigma):
    return (xl / (sigma ** 2)) * math.exp(-1 * ((xl ** 2) / (2 * (sigma ** 2))))


def base(size):
    list_r = []
    for i in range(size):
        list_r.append(random())
    return list_r


def reley_sample(sigma, b):
    M = rayleigh(sigma, sigma)
    ri = base(5000)
    x = []
    i = 1
    while i < 5000:
        X = b * ri[i]  # a = 0
        Y = M * ri[i + 1]
        if Y <= rayleigh(X, sigma):
            x.append(X)
        i += 1
        if len(x) >= 1000:
            break
    x = sorted(x)
    interval = [0, x[-1]]
    print('\nиспользовано значений r:', i)
    return x, interval

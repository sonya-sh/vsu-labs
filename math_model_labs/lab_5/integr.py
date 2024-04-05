import numpy as np
from random import random


def max_min(a, b, func):
    func_values = []
    for x in np.linspace(a, b, 1000):
        func_values.append(func(x))
    return max(func_values), min(func_values)


def trap(func, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(0, n):
        s += 0.5 * (func(a) + func(a + h)) * h
        a += h
    return s


def mc_1(func, a, b, n):
    SUM = 0
    r = []
    for j in range(n):
        r.append(random())
    for i in range(n):
        U = r[i] * (b - a) + a
        SUM += func(U)
    I = (b - a) / n * SUM
    return I


def mc_2(func, a, b, n):
    k = 0
    M, M1 = max_min(a, b, func)
    for i in range(n):
        X = a + (b - a) * random()
        Y = M1 + (M - M1) * random()
        if Y < func(X):
            k += 1
    return (M - M1) * (b - a) * (k / n)

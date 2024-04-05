from random import random


def base(size):
    list_r = []
    for i in range(size):
        list_r.append(random())
    return list_r


def normal_sample(a, b):
    global interval
    r = base(1000)
    x = []
    for ri in r:
        xi = a + (ri * (b - a))  # x = a + r(b - a)
        x.append(xi)
        x = sorted(x)
        interval = [a, b]
    return x, interval

import numpy as np
from scipy import integrate
import math

f = lambda x: x * math.e**-x
a = 0
b = 1.5
v = integrate.quad(f, a, b)


def nodes_count(method, f, a, b):
    val = v[0]
    i = 1
    n = 1
    temp = np.abs(method(f, a, b, n))
    while i > 0.11:
        i = np.abs(val - temp)
        temp = np.abs(method(f, a, b, n))
        n *= 2
    return n


def nodes_count_mc(method, f, a, b):
    val = v[0]
    i = 1
    n = 1
    temp = np.abs(method(f, a, b, n))
    while i > 0.11:
        i = np.abs(val - temp)
        temp = np.abs(method(f, a, b, n))
        n *= 100
    return n

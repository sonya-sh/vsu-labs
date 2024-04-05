import math

from integr import *
from nodes_count import *
import numpy as np
from numpy import std
import matplotlib.pyplot as plt
from scipy import integrate


f = lambda x: np.sin(1 + x/2)
a = -1
b = 4
fig = plt.subplots()
x = np.linspace(a, b, 100)
plt.plot(x, [f(_) for _ in x])

v = integrate.quad(f, a, b)
print("Аналитическое выражение I: ", round(v[0], 3))


trap_nodes = nodes_count(trap, f, a, b)
t = trap(f, a, b, trap_nodes)
print("\nМетод трапеции: ", round(t, 3))
print("Количество узлов сетки: ", trap_nodes)
print("Погрешность: ", abs(round((v[0] - t), 3)))




plt.show()

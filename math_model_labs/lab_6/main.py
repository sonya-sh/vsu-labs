from dichotomy import dichotomy_method
from chord import *
from simple_iterations import *
from Newton import *

a = 2
b = 4

A = -0.4
B = -0.2

x = np.linspace(A, B, 1000)
y1 = fun(a, b, x)
plt.plot(x, y1)
y2 = [0 for x in x]
plt.plot(x, y2)
plt.grid(True)
plt.show()

eps = 0.0001
accuracy = abs(len(str(eps))) - 2
n = int(input("Число итераций n: "))


print("\nМЕТОД ДИХОТОМИИ")
x01 = float(input("x0 для метода дихотомии: "))
dichotomy_method(x01, eps, accuracy, a, b, A, B, n)
plt.title("Метод дихотомии")
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True)
plt.show()


print("\nМЕТОД ХОРД")
x02 = float(input("x0 для метода хорд: "))
chord_method2(x02, n, a, b, eps, accuracy, A, B)
plt.title("Метод хорд")
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True)
plt.show()

y3 = fi(a, b, x)
y4 = x
print("\nМЕТОД ПРОСТЫХ ИТЕРАЦИЙ")
x03 = float(input("x0 для метода простых итераций: "))
iteration_method(x03, eps, accuracy, a, b, n)
plt.title("Метод простых итераций")
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.grid(True)
plt.show()

print("\nМЕТОД НЬЮТОНА")
x04 = float(input("x0 для метода Ньютона: "))
newton_method(x04, n, a, b, eps, accuracy)
plt.title("Метод Ньютона")
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid(True)
plt.show()

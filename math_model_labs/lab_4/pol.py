import matplotlib.pyplot as plt
import math


def pol(x, interval, p, m=0, d=0, sigma=0):
    data_pol, k = create_pol(x, interval)
    show_pol(x, data_pol, interval, p, m, d, sigma)


def create_pol(X, interval):
    a = interval[0]
    b = interval[1]
    N = len(X)
    k = 19
    dx = (b - a) / k
    data_pol = []
    for i in range(k):
        q = a + dx * (i + 1)
        count_elements = 0
        for x in X:
            if x < q:
                count_elements += 1
        F = count_elements / N
        data_pol.append([F, q])
    return data_pol, k


def F_normal(a, b, x):
    if a <= x <= b:
        return (x - a) / (b - a)
    elif x >= b:
        return 1
    else:
        return 0


def F_gauss(x, m, sigma):
    return (1 / 2) * (1 + math.erf((x - m) / math.sqrt(2 * (sigma ** 2))))


def F_rayleigh(x, sigma):
    return 1 - math.exp(-1 * (x ** 2) / (2 * sigma ** 2))


def theoretical_F(X, a, b, p, m=0, d=0, sigma=0):
    if p == 1:
        r = []
        for x in X:
            r.append(F_normal(a, b, x))
        plt.plot(X, r)
    elif p == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(F_gauss(x, m, sigma))
        plt.plot(X, r)
    elif p == 3:
        r = []
        for x in X:
            r.append(F_rayleigh(x, sigma))
        plt.plot(X, r)


def show_pol(X, data_pol, interval, p, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    x = [a]
    y = [0]
    for i in data_pol:
        y.append(i[0])
        x.append(i[1])
    plt.step(x, y)
    theoretical_F(X, a, b, p, m, d, sigma)
    plt.show()

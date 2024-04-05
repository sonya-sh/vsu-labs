import matplotlib.pyplot as plt
import math


def hist(x, interval, p, m=0, d=0, sigma=0):
    data_hist, k = create_hist(x, interval)
    show_hist(x, data_hist, k, interval, p, m, d, sigma)


def create_hist(X, interval):
    a = interval[0]
    b = interval[1]
    N = len(X)
    k = 19  # число интервалов группировки
    dx = (b - a) / k  # ширина каждого интервала
    data_hist = []
    for i in range(k + 1):
        x_min = a + dx * (i - 1)  # начало интервала
        x_max = a + dx * i  # конец интервала
        count_elements = 0  # количество элементов, попавших в интервал
        for x in X:
            if x_min < x <= x_max:
                count_elements += 1
        w = count_elements / (N * dx)  # относительная частота
        data_hist.append([w, x_min, x_max])
    return data_hist, k


def f_normal(a, b, x):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0


def f_gauss(x, m, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-1 * (x - m) ** 2 / (2 * (sigma ** 2)))


def f_rayleigh(x, sigma):
    return (x / (sigma ** 2)) * math.exp(-1 * ((x ** 2) / (2 * (sigma ** 2))))


def theoretical_f(X, a, b, p, m=0, d=0, sigma=0):
    if p == 1:
        r = []
        for x in X:
            r.append(f_normal(a, b, x))
        plt.plot(X, r)
    elif p == 2:
        r = []
        sigma = math.sqrt(d)
        for x in X:
            r.append(f_gauss(x, m, sigma))
        plt.plot(X, r)
    elif p == 3:
        r = []
        for x in X:
            r.append(f_rayleigh(x, sigma))
        plt.plot(X, r)


def show_hist(X, data_hist, k, interval, p, m=0, d=0, sigma=0):
    a = interval[0]
    b = interval[1]
    dx = (b - a) / k
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        xl = (x_max + x_min) / 2
        yl = data[0]
        plt.bar(xl, yl, width=dx)
    theoretical_f(X, a, b, p, m, d, sigma)
    plt.show()

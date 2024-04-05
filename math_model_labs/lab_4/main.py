import math
from MOF import normal_sample
from CPT import gauss_sample
from NEYMAN import reley_sample
from hist import hist
from pol import pol


def mathematical_expectation(X):
    s = 0
    for x in X:
        s += x
    return s / len(X)


def dispersion(X, m):
    s = 0
    for x in X:
        s += (x - m)**2
    return s / len(X)


def main():
    print("1 - Выборка непрерывных равно распределенных случайных величин методом обратных функций")
    print("2 - Выборка величин, распредленных по Гауссовскому закону на основе ЦПТ")
    print("3 - Выборка случайных величин, распределённых по релеевскому закону методом Неймана")

    request = input()

    if request == '1':
        a = float(input("Введите начальное значение интервала: "))
        b = float(input("Введите конечное значение интервала: "))
        x, interval = normal_sample(a, b)
        m1 = mathematical_expectation(x)
        m2 = (b + a) / 2
        print("\nМатематическое ожидание равномерного распределения (m): ", (b + a) / 2)
        print("Дисперсия равномерного распределения", round(((b - a) ** 2 / 12), 4))
        print("Первый выборочный момент:", round(m1, 4))
        print("Второй выборочный момент (m известно):", round(dispersion(x, m2), 4))
        print("Второй выборочный момент (m неизвестно):", round(dispersion(x, m1), 4))
        req = input('h - построить гистограмму \np - построить полигон \n>>')
        if req == 'h':
            hist(x, interval, 1)
        pol(x, interval, 1)

    if request == '2':
        m = float(input("Введите мат ожидание для распределения Гаусса: "))
        d = float(input("Введите дисперсию для распределения Гаусса: "))
        x, interval = gauss_sample(m, d)
        m1 = mathematical_expectation(x)
        print("\nМатематчисекое ожидание распределения Гаусса (m): ", m)
        print("Дисперсия распределения Гаусса", d)
        print("Первый выборочный момент:", round(m1, 4))
        print("Второй выборочный момент (m известно):", round(dispersion(x, m), 4))
        print("Второй выборочный момент (m неизвестно):", round(dispersion(x, m1), 4))
        req = input('h - построить гистограмму \np - построить полигон \n>>')
        if req == 'h':
            hist(x, interval, 2, m, d)
        pol(x, interval, 2, m, d)

    if request == '3':
        sigma = float(input("Введите сигму для релеевского закона: "))
        b = float(input('Ведите правую границу интервала: '))
        x, interval = reley_sample(sigma, b)
        m = math.sqrt((math.pi * (sigma ** 2)) / 2)
        print("\nМатематическое ожидание распрееделение Рэлея (m): ", m)
        print("Дисперсия распределения Рэлея: ", (2 - math.pi / 2) * (sigma ** 2))
        m1 = mathematical_expectation(x)
        print("Первый выборочный момент: ", m1)
        print("Второй выборочный момент (m известно): ", dispersion(x, m))
        print("Второй выборочный момент (m неизвестно): ", dispersion(x, m1))
        req = input('h - построить гистограмму \np - построить полигон \n>>')
        if req == 'h':
            hist(x, interval, 3, 0, 0, sigma)
        pol(x, interval, 3, 0, 0, sigma)


if __name__ == "__main__":
    main()

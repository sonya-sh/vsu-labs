import matplotlib.pyplot as plt
import numpy as np


def dataset():
    set = []
    set1 = []
    with open('data.txt') as f:
        content = f.read().split('\n')
        for i in range(len(content)):
            set.append(list(map(float, content[i].split(' '))))
        for i in range(0, len(set)-1, 2):
            set1.append([set[i], set[i+1]])
    return set1


def sorted_dataset():
    set = dataset()
    for i in range(len(set)):
        sorted_data = sorted(zip(set[i][0], set[i][1]))
        set[i][0] = [x[0] for x in sorted_data]
        set[i][1] = [x[1] for x in sorted_data]
    return set


def choose_graphs(graphs):
    selected_graphs = []
    print("Доступно графиков: {}".format(len(graphs)))
    print("Введите номер графика или несколько номеров через пробел: ")
    data = list(map(int, input().split(' ')))
    for i in data:
        selected_graphs.append(graphs[i-1])
    return selected_graphs


def gorner(n, x, a):
    p = a[n]
    for i in range(n, 0, -1):
        p = p * x
        p = p + a[i-1]
    return p


def approximation(x, y, n):
    coef_array = np.polyfit(x, y, n)  # массив коэффициентов полинома
    print("Коэффициенты полинома: \n", coef_array)
    f = np.poly1d(coef_array)  # создаётся многочлен с коэфициентами из coef_array
    print("Аппроксимирующий полином: \n", f)
    coef_list = list(coef_array)
    coef_list.reverse()
    sum = 0
    list_fx_gorner = []
    for i in range(len(x)):
        fx_gorner = gorner(n, x[i], coef_list)
        list_fx_gorner.append(fx_gorner)
        sum += (y[i] - list_fx_gorner[i])**2
    print("Значения экспериментальных точек: \n", y)
    print("Значения полинома в экспериментальных точках: \n", list_fx_gorner)
    print("Суммарная ошибка отклонения: \n", sum)
    xi = np.arange(x[0], x[len(x)-1], 0.001)
    plt.plot(xi, f(xi))
    plt.grid(True)


def show_graph(graphs):
    set = choose_graphs(graphs)
    print("Введите степень полинома: ")
    n = int(input())
    for g in set:
        x = g[0]
        y = g[1]
        approximation(x, y, n)
        plt.scatter(x, y)
    plt.show()


graph_set = sorted_dataset()
show_graph(graph_set)

import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


def dataset():
    set = []
    set1 = []
    with open('data.txt') as f:
        content = f.read().split('\n')
        for i in range(len(content)):
            set.append(list(map(float, content[i].split(' '))))
        for i in range(0, len(set) - 1, 2):
            set1.append([set[i], set[i + 1]])
    return set1


def sorted_dataset():
    set = dataset()
    for i in range(len(set)):
        sorted_data = sorted(zip(set[i][0], set[i][1]))
        set[i][0] = [x[0] for x in sorted_data]
        set[i][1] = [x[1] for x in sorted_data]
    print(set)
    print(len(set))
    return set


def choose_graphs(graphs):
    selected_graphs = []
    print("Доступно графиков: {}".format(len(graphs)))
    print("Введите номер графика или несколько номеров через пробел")
    data = list(map(int, input().split(' ')))
    for i in data:
        selected_graphs.append(graphs[i - 1])
    return selected_graphs


def show_spline_interpolation(graphs):
    set = choose_graphs(graphs)
    for g in set:
        x = g[0]
        y = g[1]
        tck = interpolate.splrep(x, y)
        xi = np.arange(x[0], x[len(x)-1], 0.001)
        yi = interpolate.splev(xi, tck)
        plt.scatter(x, y)
        plt.plot(xi, yi)
    plt.show()


graph_set = sorted_dataset()
show_spline_interpolation(graph_set)

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
    print(set)
    print(len(set))
    return set


def choose_graphs(graphs):
    selected_graphs = []
    print("Доступно графиков: {}".format(len(graphs)))
    print("Введите номер графика или несколько номеров через пробел")
    data = list(map(int, input().split(' ')))
    for i in data:
        selected_graphs.append(graphs[i-1])
    return selected_graphs


def parabolic_interpolation(x, y, xi, i):
    matrix_x = [[x[i-1]**2, x[i-1], 1],
                [x[i]**2, x[i], 1],
                [x[i+1]**2, x[i+1], 1]]
    vector_y = [y[i-1], y[i], y[i+1]]
    res = np.linalg.solve(matrix_x, vector_y)
    ai = res[0]
    bi = res[1]
    ci = res[2]
    yx = ai*xi**2 + bi*xi + ci
    return yx


def show_parabolic_interpolation(graphs):
    set = choose_graphs(graphs)
    for g in set:
        x = g[0]
        y = g[1]
        plt.scatter(x, y)
        for i in range(1, len(x)-1, 2):
            x1 = np.arange(x[i - 1], x[i + 1], 0.001)
            y1 = [parabolic_interpolation(x, y, xi, i) for xi in x1]
            plt.plot(x1, y1)
        for j in range(len(x)-1, len(x), 1):
            x1 = np.arange(x[j - 1], x[j], 0.001)
            y1 = [parabolic_interpolation(x, y, xi, j-1) for xi in x1]
            plt.plot(x1, y1)
    plt.show()


graph_set = sorted_dataset()
show_parabolic_interpolation(graph_set)

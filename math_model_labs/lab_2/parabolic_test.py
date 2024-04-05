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


def sort_dataset() -> list:
    data = dataset()
    for i in range(0, len(data), 1):
        data_s = sorted(zip(data[i][0], data[i][1]), key=lambda tup: tup[0])
        data[i][0] = [x[0] for x in data_s]
        data[i][1] = [x[1] for x in data_s]
    print(data)
    print(len(data))
    return data


def choose_graphs(graphs):
    selected_graphs = []
    print("Доступно графиков: {}".format(len(graphs)))
    print("Введите номер графика или несколько номеров через пробел")
    data = list(map(int, input().split(' ')))
    for i in data:
        selected_graphs.append(graphs[i-1])
    return selected_graphs


def parabolic(x, y, xi):
    yx = 0
    for i in range(1, len(x) - 1):
        if (x[i-1] <= xi <= x[i]) or (x[i] <= xi <= x[i+1]):
            matrix_x = [[x[i - 1] ** 2, x[i - 1], 1],
                        [x[i] ** 2, x[i], 1],
                        [x[i + 1] ** 2, x[i + 1], 1]]
            vector_y = [y[i - 1], y[i], y[i + 1]]
            res = np.linalg.solve(matrix_x, vector_y)
            ai = res[0]
            bi = res[1]
            ci = res[2]
            yx = ai * xi ** 2 + bi * xi + ci
            break
    return yx


def show_parabolic(graphs):
    set = choose_graphs(graphs)
    for g in set:
        x = np.array(g[0], dtype=float)
        y = np.array(g[1], dtype=float)
        plt.scatter(x, y)
        x1 = np.linspace(np.min(x), np.max(x), 1000)
        y1 = [parabolic(x, y, xi) for xi in x1]
        plt.plot(x1, y1)
    plt.show()


graph_set = sort_dataset()
print(graph_set)
show_parabolic(graph_set)
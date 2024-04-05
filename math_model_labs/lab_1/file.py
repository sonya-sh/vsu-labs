import matplotlib.pyplot as plt


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


def choose_graphs(graphs):
    selected_graphs = []
    print("Доступно графиков: {}".format(len(graphs)))
    print("Введите номер графика или несколько номеров через пробел")
    data = list(map(int, input().split(' ')))
    for i in data:
        selected_graphs.append(graphs[i-1])
    return selected_graphs


def show_graph(graphs):
    set = choose_graphs(graphs)
    for g in set:
        x = g[0]
        y = g[1]
        plt.scatter(x, y)
    plt.show()


graph_set = dataset()
print(graph_set)
show_graph(graph_set)
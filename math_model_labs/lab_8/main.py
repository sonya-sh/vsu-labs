from Euler import *
from RK4 import *

accuracy = 6
data_euler = Euler(0.2, 0, 1, fun, accuracy)
data_euler.pop(3)
data_rk4 = [(RK4(0.2, 0, 1, fun, accuracy))[2], (RK4(0.2, 0, 1, fun, accuracy))[3]]

max_columns = []
for col in zip(*data_rk4):
    len_el = []
    [len_el.append(len(str(el))) for el in col]
    max_columns.append(max(len_el))

for el in data_euler:
    for col in el:
        print(f'{col:{max(max_columns)+1}}', end='')
    print()

for el in data_rk4:
    for col in el:
        print(f'{col:{max(max_columns)+1}}', end='')
    print()


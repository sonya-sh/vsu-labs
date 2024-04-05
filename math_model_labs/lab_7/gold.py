def golden_ratio(f, a, b, eps):
    global x
    fi = 1.6180339887
    n = 1
    while abs(b - a) >= eps:
        x1 = b - (b - a) / fi
        x2 = a + (b - a) / fi
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        n += 1
        x = (a + b) / 2
    return x, n

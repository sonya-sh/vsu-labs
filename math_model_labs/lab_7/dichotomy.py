def dichotomy_method(f, a, b, eps):
    global x
    d = eps
    n = 0
    while abs(b - a) >= eps:
        x = (a + b) / 2
        if f(x - d/2) < f(x + d/2):
            b = x
        else:
            a = x
        n += 2
        x = (a + b) / 2
    return x, n

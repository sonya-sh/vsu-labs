def F(n):
    if n in (1, 2):
        return 1
    return F(n - 1) + F(n - 2)


def fib(f, a, b, eps, n):
    global x
    n0 = n
    x1 = a + (b - a) * F(n) / F(n + 2)
    x2 = a + (b - a) * F(n + 1) / F(n + 2)
    while n != 1:
        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = b - x1 + a
        else:
            b = x2
            x2 = x1
            x1 = a + b - x2
        n -= 1
        x = (x1 + x2) / 2
    return x, n0

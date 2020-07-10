def null(*args):
    return 0


def succ(n):
    return n + 1


def pred(n):
    return n - 1


def proj(n):
    def f(*args):
        return args[n]
    return f


# composition
def C(g, *func):
    def f(*args):
        return g(*[h(*args) for h in func])
    return f


# primitive recursion
def R(g, h):
    def f(*args):
        if args[0] == 0:
            return g(*args[1:])
        else:
            return h(R(g, h)(*(args[0] - 1, *args[1:])), *(args[0] - 1, *args[1:]))

    return f

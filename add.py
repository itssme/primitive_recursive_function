from primitive_recursive_function import *


def add(n, m):
    return R(proj(0), C(succ, proj(0)))(n, m)


if __name__ == '__main__':
    n = int(input("?: "))
    m = int(input("?: "))

    print(str(n) + " + " + str(m) + " = " + str(add(n, m)))
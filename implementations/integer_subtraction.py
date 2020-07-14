from primitive_recursive_function import *


def sub(n: int, m: int) -> int:
    return C(R(proj(0), C(pred, proj(0))), proj(1), proj(0))(n, m)


if __name__ == '__main__':
    n = int(input("?: "))
    m = int(input("?: "))

    print(str(n) + " - " + str(m) + " = " + str(sub(n, m)))

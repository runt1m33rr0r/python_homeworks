import math


def f(x):
    return  x * x * x + 3 * x - 5


def f2(x):
    return math.exp(x) - 2 * x - 2


def f3(x):
    return x ** 3 + 3 * x - 5


def bisection(a, b, func):
    delta = 0.001

    # if signs are different, throw exception(no solution)
    if func(b) * func(a) < 0:
        while True:
            found_mid = False
            mid = 0
            current_distance = 0
            previous_distance = 0

            mid = (a + b) / 2.0
            if func(b) * func(mid) > 0:
                b = mid
            else:
                a = mid

            found_mid = func(mid) == 0
            previous_distance = current_distance
            current_distance = abs(a - b)

            if current_distance <= delta or current_distance == previous_distance or found_mid != False:
                return mid
    else:
        raise ValueError("No solution!")


def get_interval(a_str, b_str):
    try:
        a = float(a_str)
    except ValueError:
        raise ValueError('a is not a number')

    try:
        b = float(b_str)
    except ValueError:
        raise ValueError('b is not a number')
    
    return float(a), float(b)


if __name__ == '__main__':
    a, b = get_interval(raw_input('a: '), raw_input('b: '))
    result = bisection(a, b, f)
    print result
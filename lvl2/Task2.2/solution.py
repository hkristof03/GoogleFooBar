from collections import Counter


def numberToBase(n, b):
    """"""
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(str(int(n % b)))
        n //= b
    return digits[::-1]


def assign_tasks(n, b):
    """"""
    k = len(n)

    x = sorted(n, reverse=True, key=int)
    x = ''.join(x)
    y = sorted(n, key=int)
    y = ''.join(y)

    x_int = int(x, b)
    y_int = int(y, b)

    z = x_int - y_int
    z = ''.join(numberToBase(z, b))

    diff = k - len(z)
    if diff:
        z = '0'* diff + z

    return z


def solution(n, b):
    """"""
    assert (b >= 2) and (b <= 10)
    assert (len(n) >= 2) and (len(n) <= 9)

    if len(set(n)) == 1:
        return 1

    l = []

    while True:

        n = assign_tasks(n, b)

        l.append(n)
        d_ = dict(Counter(l))
        frequencies = sorted(d_.values(), reverse=True)

        if frequencies[0] > 2:

            length = frequencies.count(2)
            cycle_length = length + 1 if length else 1

            return cycle_length


if __name__ == '__main__':

    assert solution('210022', 3) == 3

    assert solution('1211', 10) == 1

    assert solution('1111', 10) == 1

    assert solution('0000', 10) == 1

    assert solution('210022', 3) == 3

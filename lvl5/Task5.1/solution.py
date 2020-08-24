from decimal import Decimal, getcontext

getcontext().prec = 101
CONST = Decimal(2).sqrt() - 1

def solution(n):

    n = long(n)

    def func(n):

        if n == 0:
            return form
        if n < 0:
            return 0
        else:
            n_ = long(CONST * n)
            return n*n_ + n*(n+1)/2 - n_*(n_+1)/2 - func(n_)

    return str(func(n))


if __name__ == '__main__':

    assert solution('5') == '19'

    assert solution('77') == '4208'

from timeit import default_timer as timer
from operator import xor

from numba import jit


# Function to return the XOR of elements
# from the range [1, n]
@jit(nopython=True)
def findXOR(n):
    mod = n % 4;

    # If n is a multiple of 4
    if (mod == 0):
        return n;

    # If n % 4 gives remainder 1
    elif (mod == 1):
        return 1;

    # If n % 4 gives remainder 2
    elif (mod == 2):
        return n + 1;

    # If n % 4 gives remainder 3
    elif (mod == 3):
        return 0;

# Function to return the XOR of elements
# from the range [l, r]
@jit(nopython=True)
def findXORFun(l, r):
    return (xor(findXOR(l - 1) , findXOR(r)))

@jit(nopython=True)
def solution(start, length):
    """"""
    assert start >= 0 and start <= 2000000000
    assert length >= 1

    if length == 1:
        return start

    else:

        begin = start
        end = length

        cumsum = -1

        while end != 0:

            if length != 1:

                res = findXORFun(begin, begin + end -1)
                end -= 1
                begin += length

                if cumsum == -1:
                    cumsum = res

                else:
                    cumsum = xor(cumsum, res)

            else:
                cumsum = xor(cumsum, begin)

        return cumsum


if __name__ == '__main__':

    s = timer()

    start = 2000000
    length = 1000000

    res = solution(start, length)
    assert res == 1036149002240

    e = timer()

    print(f"Done in {e-s} seconds")

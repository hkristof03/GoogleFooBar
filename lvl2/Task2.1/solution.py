def solution(l, t):

    length = len(l)
    assert (length >= 1) and (length <= 100)
    for i in range(length):
        assert (l[i] >= 1) and (l[i] <= 100)
    assert isinstance(t, int) and (t <= 250)

    sum_l = sum(l)

    if sum_l < t:
        return [-1, -1]

    for i in range(length):

        if i == t:
            return [i, i]

        for j in range(i + 1, length + 1):

            if sum(l[i:j]) == t:
                return [i, j-1]

    return [-1, -1]


if __name__ == '__main__':

    assert solution([1,2,3,4], 15) == [-1, -1]

    assert solution([4, 3, 10, 2, 8], 12) == [2, 3]

    assert solution([2], 2) == [0, 0]

    assert solution([1,2], 3) == [0, 1]

    assert solution([1,2,3], 6) == [0, 2]

    assert solution([5,6,1,2], 3) == [2, 3]

    assert solution([56, 2, 3, 4, 88], 7) == [2, 3]

    assert solution([88, 99, 66, 55, 10], 65) == [3, 4]

    assert solution([1, 6, 3, 4, 5], 5) == [4, 4]

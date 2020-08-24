def solution(l):
    """"""
    counter = 0
    map1 = {}
    map2 = {}

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if not l[j] % l[i]:
                map1[j] = map1.get(j, 0) + 1
                map2[i] = map2.get(i, 0) + 1

    for i in map1.keys():
        counter += map1.get(i, 0) * map2.get(i, 0)

    return counter


if __name__ == '__main__':

    assert solution([1,2,3,4,5,6]) == 3

    assert solution([1,1,1]) == 1

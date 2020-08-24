def detectLoop(x, y):
    """"""
    n = x + y
    while n % 2 == 0:
        n /= 2
    return x % n != 0

class GFG:
    def __init__(self,graph):
        self.graph = graph
        self.rows = len(graph)
        self.cols = len(graph[0])

    def bpm(self, u, matchR, seen):
        """"""
        for v in range(self.cols):
            if self.graph[u][v] and seen[v] == False:
                # Mark v as visited
                seen[v] = True
                condition = (matchR[v] == -1) or (self.bpm(matchR[v], matchR, seen))
                if condition:
                    matchR[v] = u
                    return True
        return False

    # Returns maximum number of matching
    def maxBPM(self):
        """"""
        matchR = [-1] * self.cols
        result = 0
        for i in range(self.rows):
            seen = [False] * self.cols

            if self.bpm(i, matchR, seen):
                result += 1
        return result

def createEdmondsMatrix(banana_list):
    """"""
    n_guards = len(banana_list)

    assert n_guards >= 1 and n_guards <= 100
    assert all(x > 0 and x <= 1073741823 for x in banana_list)

    edmonds_matrix = [[0 for i in range(n_guards)] for j in range(n_guards)]

    for i in range(n_guards):
        for j in range(n_guards):
            if i == j:
                continue
            if i < j:
                edmonds_matrix[i][j] = 1 if detectLoop(banana_list[i], banana_list[j]) else 0
            if j < i:
                edmonds_matrix[i][j] = edmonds_matrix[j][i]

    return edmonds_matrix

def solution(banana_list):
    """"""
    edmonds_matrix = createEdmondsMatrix(banana_list)
    max_matching = GFG(edmonds_matrix).maxBPM()
    return len(banana_list) - max_matching


if __name__ == '__main__':

    assert solution([1, 7, 3, 21, 13, 19]) == 0

    assert solution([1, 1]) == 2

    assert solution([1]) == 1

    assert solution([1, 7, 1, 1]) == 4

    assert solution([1, 2, 1, 7, 3, 21, 13, 19]) == 0

    assert solution([5]) == 1

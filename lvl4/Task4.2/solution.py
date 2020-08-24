import itertools

class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def BellmanFord(self, src):
        """"""
        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        # Check negative cycle existence
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        return []
        # return shortest distances from source
        return dist

def createGraph(m):
    """"""
    graph = Graph(len(m))
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if m[i][j]:
                graph.addEdge(i, j, m[i][j])
    return graph

def calculate_path_cost(matrix_sp, path):
    """"""
    cost = 0
    for p_ in path:
        cost += matrix_sp[p_[0]][p_[1]]
    return cost

def solution(times, t):
    """"""
    n_bunnies = len(times) - 2

    # check time travel (no path costs)
    if all(i == 0 for i in list(itertools.chain(*times))):
        return list(range(n_bunnies))

    graph = createGraph(times)
    # matrix of shortest paths from sources
    matrix_sp = []
    for i in range(len(times)):
        sps = graph.BellmanFord(i)
        if sps:
            matrix_sp.append(sps)
        else:
            # has a negative cycle
            return list(range(n_bunnies))

    if matrix_sp:

        length_permutations = 0
        good_permutations = []

        for i in reversed(range(n_bunnies + 1)):

            n_bunnies_permutations = itertools.permutations(range(1, n_bunnies + 1), i)

            for perm in n_bunnies_permutations:

                p_ = [0] + list(perm) + [-1]
                path = [(p_[i-1], p_[i]) for i in range(1, len(p_))]

                cost = calculate_path_cost(matrix_sp, path)

                if good_permutations and (len(perm) < length_permutations):
                    return sorted([i-1 for i in set(itertools.chain(*good_permutations))])[:length_permutations]

                if cost <= t:
                    good_permutations.append(perm)
                    length_permutations = len(perm)
    return []


if __name__ == '__main__':

    assert (
        solution(
            [
                [0, 2, 2, 2, -1],
                [9, 0, 2, 2, -1],
                [9, 3, 0, 2, -1],
                [9, 3, 2, 0, -1],
                [9, 3, 2, 2, 0]
            ],
            1
        ) == [1, 2]
    )

    assert (
        solution(
            [
                [0, 1, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 1, 0]
            ],
            3
        ) == [0, 1]
    )

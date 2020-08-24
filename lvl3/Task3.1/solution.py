from collections import deque
import copy


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QueueNode:
    def __init__(self, pt, dist):
        self.pt = pt
        self.dist = dist

def isValid(row, col, ROWS, COLS):
    return (row >= 0) and (row < ROWS) and (col >= 0) and (col < COLS)

def BFS(mat, src, dst, ROWS, COLS):

    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]

    visited = [[False for i in range(COLS)] for j in range(ROWS)]

    # Mark the source cell as visited
    visited[src.x][src.y] = True

    # Create a queue for BFS
    q = deque()

    # Distance of source cell is 1
    s = QueueNode(src, 1)
    q.append(s) #  Enqueue source cell

    # Do a BFS starting from source cell
    while q:

        curr = q.popleft() # Dequeue the front cell

        # If we have reached the destination cell,
        # we are done
        pt = curr.pt
        if (pt.x == dst.x) and (pt.y == dst.y):
            return curr.dist

        # Otherwise enqueue its adjacent cells
        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            # if adjacent cell is valid, has path
            # and not visited yet, enqueue it.
            if isValid(row, col, ROWS, COLS) and mat[row][col] == 0 and not visited[row][col]:

                visited[row][col] = True
                Adjcell = QueueNode(Point(row,col), curr.dist + 1)
                q.append(Adjcell)

    # Return a large number if destination can not be reached
    return 999999999

def get_walls_positions(m, ROWS, COLS):

    walls = []
    for i in range(ROWS):
        for j in range(COLS):
            value = m[i][j]
            if value:
                walls.append(Point(i, j))

    return walls

def remove_wall(m, wall):
    """"""
    m_ = copy.deepcopy(m)
    x = wall.x
    y = wall.y
    m_[x][y] = 0

    return m_

def solution(m):
    """"""
    ROWS = len(m)
    COLS = len(m[0])

    src = Point(0, 0)
    dst = Point(ROWS-1, COLS-1)

    path_costs = set([])

    pc = BFS(m, src, dst, ROWS, COLS)
    path_costs.add(pc)

    walls = get_walls_positions(m, ROWS, COLS)

    for wall in walls:
        m_ = remove_wall(m, wall)
        pc = BFS(m_, src, dst, ROWS, COLS)
        if pc not in path_costs:
            path_costs.add(pc)

    shortest_path = min(path_costs)

    return shortest_path


if __name__ == '__main__':

    m = [
        [0,0,0,0,0,0],
        [1,1,1,1,1,0],
        [0,0,0,0,0,0],
        [0,1,1,1,1,1],
        [0,1,1,1,1,1],
        [0,0,0,0,0,0]
    ]
    assert solution(m) == 11

    m = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
    assert solution(m) == 7

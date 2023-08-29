import sys
from collections import deque


class Node:

    def __init__(self, row, col, depth):
        self.row = row
        self.col = col
        self.depth = depth


def solution(n, m, grid):
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    start = Node(0, 0, 0)
    way_queue = deque([start])
    wall_queue = deque()

    while way_queue or wall_queue:
        way_queue.popleft()


n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
print(solution(n, m, grid))
import sys
from collections import deque


def solution(n, m, grid):
    distances = [[-1] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    distance = 0
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j))
                visited[i][j] = True
            elif grid[i][j] == 0:
                distances[i][j] = 0

    while q:
        for _ in range(len(q)):
            row, col = q.popleft()
            distances[row][col] = distance

            for i in range(4):
                delta_row, delta_col = delta[i]
                new_row = row + delta_row
                new_col = col + delta_col

                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                    continue

                if not visited[new_row][new_col] and grid[new_row][new_col] != 0:
                    q.append((new_row, new_col))
                    visited[new_row][new_col] = True

        distance += 1

    return distances


n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = solution(n, m, grid)

for i in range(n):
    for j in range(m):
        print(result[i][j], end=' ')
    print()

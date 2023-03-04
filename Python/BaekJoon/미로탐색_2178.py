import sys
from collections import deque


def solution(N, M, maze):
    breadth = 1
    delta_row = [1, -1, 0, 0]
    delta_col = [0, 0, 1, -1]
    visited = [[False] * M for _ in range(N)]
    q = deque([(0, 0)])

    while q:
        for _ in range(len(q)):
            row, col = q.popleft()

            if row == N - 1 and col == M - 1:
                return breadth

            for i in range(4):
                next_row = row + delta_row[i]
                next_col = col + delta_col[i]

                if next_row < 0 or next_row > N-1 or next_col < 0 or next_col > M-1:
                    continue

                if visited[next_row][next_col]:
                    continue

                if maze[next_row][next_col] == 1:
                    q.append((next_row, next_col))
                    visited[next_row][next_col] = True
        breadth += 1


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

print(solution(N, M, maze))

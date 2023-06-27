import sys
from collections import deque


def solution(n, grid):
    answer = 0
    delta = [(1, 0), (0, 1)]
    q = deque([(0, 0)])

    while q:
        answer *= len(q)

        for _ in range(len(q)):
            row, col = q.popleft()

            if row == n - 1 and col == n - 1:
                answer += 1
                continue

            for row_delta, col_delta in delta:
                new_row = row + row_delta * grid[row][col]
                new_col = col + col_delta * grid[row][col]

                if new_row >= n or new_col >= n:
                    continue

                q.append((new_row, new_col))

    return answer


n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, grid))


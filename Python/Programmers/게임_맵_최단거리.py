from collections import deque


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        for _ in range(len(q)):
            row, col = q.popleft()

            if row == n - 1 and col == m - 1:
                return answer + 1

            for i in range(4):
                delta_row, delta_col = delta[i]

                new_row = row + delta_row
                new_col = col + delta_col

                if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                    continue

                if not visited[new_row][new_col] and maps[new_row][new_col] == 1:
                    visited[new_row][new_col] = True
                    q.append((new_row, new_col))
        answer += 1
    return -1

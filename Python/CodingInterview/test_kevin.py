from collections import deque


def can_reach(island, row, col):
    q = deque()
    n = len(island)
    visited = [[False] * n for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q.append((row, col))

    while q:
        current_row, current_col = q.popleft()
        visited[current_row][current_col] = True

        for i in range(4):
            next_row = current_row + dx[i]
            next_col = current_col + dy[i]

            if next_row < 0 or next_row >= n or next_col < 0 or next_row >= n:
                return True

            if island[next_row][next_col] <= island[current_row][current_col] and not visited[next_row][next_col]:
                q.append((next_row, next_col))

    return False

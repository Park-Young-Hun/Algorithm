import sys
from collections import deque


def bfs(area, start, criteria):
    global visited
    q = deque([start])
    n = len(area)

    ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        row, col = q.popleft()

        for way in ways:
            delta_row, delta_col = way

            next_row = row + delta_row
            next_col = col + delta_col

            if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n:
                continue
            if visited[next_row][next_col]:
                continue

            if area[next_row][next_col] > criteria:
                q.append((next_row, next_col))
                visited[next_row][next_col] = True


def solution(N, area):
    answer = []
    global visited

    for criteria in range(0, 101):
        cnt = 0
        visited = [[False] * N for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if not visited[i][j] and area[i][j] > criteria:
                    bfs(area, (i, j), criteria)
                    cnt += 1
        answer.append(cnt)
    return max(answer)


N = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
global visited

print(solution(N, area))

import sys


def melt(ice):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    water_cnt = [[0] * m for _ in range(n)]

    for row, col in ice:
        for i in range(4):
            delta_row, delta_col = delta[i]

            new_row = row + delta_row
            new_col = col + delta_col

            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                continue

            if north_pole[new_row][new_col] == 0:
                water_cnt[row][col] += 1

    for row, col in ice:
        north_pole[row][col] -= water_cnt[row][col]
        if north_pole[row][col] < 0:
            north_pole[row][col] = 0


def dfs(row, col):
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(4):
        delta_row, delta_col = delta[i]

        new_row = row + delta_row
        new_col = col + delta_col

        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
            continue

        if not visited[new_row][new_col] and north_pole[new_row][new_col] > 0:
            visited[new_row][new_col] = True
            dfs(new_row, new_col)
    return


def solution(n, m, north_pole):
    global visited
    year = 0

    while True:
        ice = []
        visited = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if north_pole[i][j] > 0:
                    ice.append((i, j))
        if not ice:  # 모두 녹았다면
            break

        dfs(ice[0][0], ice[0][1])  # DFS로 이어진 부분을 다 탐색했는데

        for row, col in ice:
            if not visited[row][col]:  # 얼음이 남아있다면
                return year  # 빙산이 분리된 것이다.

        melt(ice)
        year += 1

    return 0


sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
north_pole = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solution(n, m, north_pole))

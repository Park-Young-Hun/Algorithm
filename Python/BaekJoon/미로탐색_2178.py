import sys


def dfs(start):
    global cnt
    delta_row = [1, -1, 0, 0]
    delta_col = [0, 0, 1, -1]

    row, col = start
    visited[row][col] = True
    cnt += 1

    if row == N-1 and col == M-1:
        answer.append(cnt)
        return

    for i in range(4):
        next_row = row + delta_row[i]
        next_col = col + delta_col[i]

        if 0 <= next_row < N and 0 <= next_col < M and maze[next_row][next_col] == 1 and not visited[next_row][next_col]:
            dfs((next_row, next_col))
            visited[next_row][next_col] = False
            cnt -= 1
    return


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline())[:-1])) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = []

global cnt
cnt = 0

dfs((0, 0))

print(min(answer))

import sys


def solution(N, M, maze):
    cnt = -1
    answer = []
    stack = [(0, 0)]
    delta_row = [1, -1, 0, 0]
    delta_col = [0, 0, 1, -1]
    visited = [[False] * M for _ in range(N)]

    while stack:
        row, col = stack.pop()
        visited[row][col] = True
        cnt += 1

        if row == N-1 and col == M-1:
            answer.append(cnt)
            cnt -= 1
            visited[row][col] = False

        for i in range(4):
            next_row = row + delta_row[i]
            next_col = col + delta_col[i]

            if 0 <= next_row < N and 0 <= next_col < M and maze[next_row][next_col] == 1 and not visited[next_row][next_col]:
                stack.append((next_row, next_col))


N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline())[:-1])) for _ in range(N)]

print(maze)

solution(N, M, maze)

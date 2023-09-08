import sys

sys.setrecursionlimit(10 ** 4)


def dfs(row, col, food):
    n = len(grid)
    m = len(grid[0])
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    food += int(grid[row][col])

    for i in range(len(delta)):
        delta_row, delta_col = delta[i]

        new_row = row + delta_row
        new_col = col + delta_col

        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
            continue

        if grid[new_row][new_col] == 'X':
            continue

        if not visited[new_row][new_col]:
            visited[new_row][new_col] = True
            food = dfs(new_row, new_col, food)

    return food


def solution(maps):
    global visited
    global grid

    answers = []
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]
    grid = list(map(list, maps))

    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                answers.append(dfs(i, j, answer))

    if not answers:
        answers.append(-1)

    answers.sort()

    return answers

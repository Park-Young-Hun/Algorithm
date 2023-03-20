import sys


def make_in_bound(n, pos):
    if pos < 0:
        return pos + n
    elif pos >= n:
        return pos - n
    else:
        return pos


def solution(n, m, grid, cmd):
    delta = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]

    for d, s in cmd:
        visited = [[False] * n for _ in range(n)]

        for i in range(len(cloud)):  # 구름 이동 및 비 내리기.
            delta_row, delta_col = delta[d - 1]

            new_row = make_in_bound(n, cloud[i][0] + s * delta_row % n)
            new_col = make_in_bound(n, cloud[i][1] + s * delta_col % n)

            grid[new_row][new_col] += 1
            visited[new_row][new_col] = True
            cloud[i][0] = new_row
            cloud[i][1] = new_col

        while cloud:  # 물 복사 마법.
            cnt = 0
            row, col = cloud.pop()

            for i in range(4):
                delta_row, delta_col = delta[2 * i + 1]
                target_row = row + delta_row
                target_col = col + delta_col

                if 0 <= target_row < n and 0 <= target_col < n:
                    if grid[target_row][target_col] > 0:
                        cnt += 1

            grid[row][col] += cnt

        for i in range(n):  # 새로운 구름 생성.
            for j in range(n):
                if grid[i][j] >= 2 and not visited[i][j]:
                    cloud.append([i, j])
                    grid[i][j] -= 2
    sum_water = 0
    for row in grid:
        sum_water += sum(row)
    return sum_water


n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cmd = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

print(solution(n, m, grid, cmd))

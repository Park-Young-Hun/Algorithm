import sys


def dfs(row, col):
    global answer
    global is_reached

    delta = [(-1, 1), (0, 1), (1, 1)]  # 위로 최대한 떙겨서 탐색(그리디)

    if col == c-1:
        answer += 1
        is_reached = True
        return

    for delta_row, delta_col in delta:
        new_row = row + delta_row
        new_col = col + delta_col

        if new_row < 0 or new_row >= r or new_col < 0 or new_col >= c:
            continue

        if grid[new_row][new_col] != 'x' and not visited[new_row][new_col]:
            visited[new_row][new_col] = True
            dfs(new_row, new_col)

            if is_reached:  # 도달 했다면 해당 DFS 탐색 아예 종료.
                return

            #visited[new_row][new_col] = False
            # 도달 못한 곳은 다른 곳을 통해 와도 어차피 도달 못하기 때문에 백트래킹 해 줄 필요 없다.
            # 그래야 시간초과 뚫을 수 있음.


def solution(grid):
    global answer
    global visited
    global is_reached

    answer = 0
    visited = [[False] * c for _ in range(r)]

    for i in range(r):
        is_reached = False
        dfs(i, 0)

    return answer


r, c = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
print(solution(grid))

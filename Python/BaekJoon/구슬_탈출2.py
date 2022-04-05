import sys

n, m = map(int, sys.stdin.readline().split())

board = [list(sys.stdin.readline())[:-1] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

for i in board:
    print(i)
print()


def dfs(table, r_pos, b_pos, cnt):
    for i in range(4):
        new_x = r_pos[0] + dx[i]
        new_y = r_pos[1] + dy[i]

        if table[new_x][new_y] == '.':
            table[r_pos[0]][r_pos[1]] = '.'

            while table[new_x][new_y] == '.':
                r_pos[0] = new_x
                r_pos[1] = new_y
                new_x += dx[i]
                new_y += dy[i]

            cnt += 1
            #if table[new_x][new_y] == 'O':



    return table

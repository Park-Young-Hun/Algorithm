import sys
from copy import deepcopy

r, c, time = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cleaner = []
answer = 0


def spread(room):
    new_room = deepcopy(room)
    for i in range(r):
        for j in range(c):

            if room[i][j] == -1:
                cleaner.append(i)

            if room[i][j] >= 5:
                piece = room[i][j] // 5
                for k in range(4):
                    new_row = i + dx[k]
                    new_col = j + dy[k]

                    if new_row < 0 or new_row >= r or new_col < 0 or new_col >= c:
                        continue
                    if room[new_row][new_col] == -1:
                        continue

                    new_room[new_row][new_col] += piece
                    new_room[i][j] -= piece
    return new_room


def clean(room):
    ex_cell = 0
    for j in range(1, c):
        temp_cell = room[cleaner[0]][j]
        room[cleaner[0]][j] = ex_cell
        ex_cell = temp_cell

    for i in range(cleaner[0]-1, -1, -1):
        temp_cell = room[i][c-1]
        room[i][c-1] = ex_cell
        ex_cell = temp_cell

    for j in range(c-2, -1, -1):
        temp_cell = room[0][j]
        room[0][j] = ex_cell
        ex_cell = temp_cell

    for i in range(1, cleaner[0]):
        temp_cell = room[i][0]
        room[i][0] = ex_cell
        ex_cell = temp_cell

    ex_cell = 0
    for j in range(1, c):
        temp_cell = room[cleaner[1]][j]
        room[cleaner[1]][j] = ex_cell
        ex_cell = temp_cell

    for i in range(cleaner[1] + 1, r):
        temp_cell = room[i][c-1]
        room[i][c-1] = ex_cell
        ex_cell = temp_cell

    for j in range(c - 2, -1, -1):
        temp_cell = room[r-1][j]
        room[r-1][j] = ex_cell
        ex_cell = temp_cell

    for i in range(r - 2, cleaner[1], -1):
        temp_cell = room[i][0]
        room[i][0] = ex_cell
        ex_cell = temp_cell
    return room


while time != 0:
    room = clean(spread(room))
    time -= 1

for i in range(r):
    for j in range(c):
        if room[i][j] > 0:
            answer += room[i][j]
print(answer)

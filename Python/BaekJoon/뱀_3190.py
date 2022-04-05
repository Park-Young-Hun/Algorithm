import sys


def set_tail(tail_pos, ways):
    if ways == "right":
        tail_pos[1] += 1
    elif ways == "down":
        tail_pos[0] += 1
    elif ways == "left":
        tail_pos[1] -= 1
    else:
        tail_pos[0] -= 1
    return tail_pos


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

apple = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]

l = int(sys.stdin.readline())
rotate = [sys.stdin.readline().split() for _ in range(l)]

board = []
head = [0, 0]
tail = [0, 0]
time = 0
direction = ["right", "down", "left", "up"]
way = []
d_idx = 0
l_idx = 0

for i in range(n):
    temp = []
    for j in range(n):
        if [i+1, j+1] in apple:
            temp.append(2)
        else:
            temp.append(0)
    board.append(temp)


board[head[0]][head[1]] = 1


while True:
    # for i in board:
    #     print(i)
    # print()
    time += 1

    if direction[d_idx] == "right" and head[1] < n-1:
        way.append(direction[d_idx])
        if board[head[0]][head[1]+1] == 2:
            board[head[0]][head[1]+1] = 1
        elif board[head[0]][head[1]+1] == 0:
            board[head[0]][head[1]+1] = 1
            board[tail[0]][tail[1]] = 0

            next_tail = way.pop(0)
            tail = set_tail(tail, next_tail)
        else:
            break
        head[1] += 1
    elif direction[d_idx] == "down" and head[0] < n-1:
        way.append(direction[d_idx])
        if board[head[0]+1][head[1]] == 2:
            board[head[0]+1][head[1]] = 1
        elif board[head[0]+1][head[1]] == 0:
            board[head[0]+1][head[1]] = 1
            board[tail[0]][tail[1]] = 0

            next_tail = way.pop(0)
            tail = set_tail(tail, next_tail)
        else:
            break
        head[0] += 1
    elif direction[d_idx] == "left" and head[1] > 0:
        way.append(direction[d_idx])
        if board[head[0]][head[1]-1] == 2:
            board[head[0]][head[1]-1] = 1
        elif board[head[0]][head[1]-1] == 0:
            board[head[0]][head[1]-1] = 1
            board[tail[0]][tail[1]] = 0

            next_tail = way.pop(0)
            tail = set_tail(tail, next_tail)
        else:
            break
        head[1] -= 1
    elif direction[d_idx] == "up" and head[0] > 0:
        way.append(direction[d_idx])
        if board[head[0]-1][head[1]] == 2:
            board[head[0]-1][head[1]] = 1
        elif board[head[0]-1][head[1]] == 0:
            board[head[0]-1][head[1]] = 1
            board[tail[0]][tail[1]] = 0

            next_tail = way.pop(0)
            tail = set_tail(tail, next_tail)
        else:
            break

        head[0] -= 1
    else:
        break

    if time == int(rotate[l_idx][0]):
        if rotate[l_idx][1] == 'D':
            d_idx = (d_idx + 1) % 4
        else:
            d_idx -= 1
            if d_idx < 0:
                d_idx = 3
        if l_idx < l-1:
            l_idx += 1

print(time)

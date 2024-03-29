def solution(places):
    answer = []
    global dx
    global dy
    global room
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = 5

    for place in places:
        flag = False
        room = [list(i) for i in place]

        for i in range(n):
            for j in range(n):
                if room[i][j] == 'P':
                    if firstSearch(i, j) == 0:
                        flag = True
                        break
            if flag:
                break
        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer


def firstSearch(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 5 and 0 <= ny < 5:
            if room[nx][ny] == 'P':
                return 0
            elif room[nx][ny] == 'O':
                if secondSearch(nx, ny, x, y) == 0:
                    return 0


def secondSearch(x, y, start_x, start_y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 5 and 0 <= ny < 5 and (nx != start_x or ny != start_y):
            if room[nx][ny] == 'P':
                return 0
    return 1

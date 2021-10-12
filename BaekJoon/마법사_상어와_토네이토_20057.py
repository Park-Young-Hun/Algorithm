import sys

# 모래 이동
left = [[0, -2, 0.05], [1, -1, 0.1], [-1, -1, 0.1], [1, 0, 0.07], [-1, 0, 0.07], [2, 0, 0.02], [-2, 0, 0.02],
        [1, 1, 0.01], [-1, 1, 0.01], [0, -1, 1]]
right = [[r, -c, ratio] for r, c, ratio in left]
up = [[c, r, ratio] for r, c, ratio in left]
down = [[-c, r, ratio] for r, c, ratio in left]


def blow(tr, tc, dir):
    global ans
    tmp = 0
    if dir == 0:
        for r, c, ratio in left:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    if dir == 1:
        for r, c, ratio in down:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    if dir == 2:
        for r, c, ratio in right:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    if dir == 3:
        for r, c, ratio in up:
            if ratio == 1:
                move_sand = sand[tr][tc] - tmp
            else:
                move_sand = int(sand[tr][tc] * ratio)
                tmp += move_sand
            if 0 <= tr + r < N and 0 <= tc + c < N:
                sand[tr + r][tc + c] += move_sand
            else:
                ans += move_sand

    sand[tr][tc] = 0


def move(tr, tc):
    # 좌 하 우 상
    dir = 0
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    while tr != 0 or tc != 0:
        nr = tr + dr[dir]
        nc = tc + dc[dir]
        if not visit[nr][nc]:
            visit[nr][nc] = 1
            tr, tc = nr, nc
            blow(tr, tc, dir)
            dir += 1
            if dir == 4:
                dir = 0
        else:
            dir -= 1
            if dir < 0:
                dir = 3


ans = 0
N = int(sys.stdin.readline())
sand = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [([0] * N) for _ in range(N)]
tr, tc = N // 2, N // 2
visit[tr][tc] = 1

move(tr, tc)

print(ans)

def solution(n, sand_map):
    target = [n // 2, n // 2]
    end = [0, 0]

    move = ["left", "down", "right", "up"]
    index = 0
    way = move[index % 4]

    stride = 1

    while True:

        for _ in range(2):
            # print(target)
            # print(way)
            if way == "left":
                target[1] -= stride
                sand_map = scatter(target, way, sand_map)
            elif way == "down":
                target[0] += stride
            elif way == "right":
                target[1] += stride
            else:
                target[0] -= stride

            if target == end:
                return out

            index += 1
            way = move[index % 4]

        if stride < n - 1:
            stride += 1

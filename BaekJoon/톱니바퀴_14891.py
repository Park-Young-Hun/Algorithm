import sys


gears = [list(map(int, sys.stdin.readline()[:-1])) for i in range(4)]
rotates_num = int(sys.stdin.readline())
rotates = [list(map(int, sys.stdin.readline().split())) for i in range(rotates_num)]


def rotate(gear_num, direction, rotated):
    if rotated[gear_num] == 1:
        return

    rotated[gear_num] = 1

    if 0 < gear_num <= 3:
        left = gear_num - 1
        if gears[gear_num][6] != gears[left][2]:
            rotate(left, -direction, rotated)
    if 0 <= gear_num < 3:
        right = gear_num + 1
        if gears[gear_num][2] != gears[right][6]:
            rotate(right, -direction, rotated)

    if direction == 1:
        temp1 = gears[gear_num][-1]
        for i in range(len(gears[0])):
            temp2 = gears[gear_num][i]
            gears[gear_num][i] = temp1
            temp1 = temp2
    else:
        temp1 = gears[gear_num][0]
        for i in range(len(gears[0]) - 1, -1, -1):
            temp2 = gears[gear_num][i]
            gears[gear_num][i] = temp1
            temp1 = temp2
    return


for i in rotates:
    rotated_flag = [0, 0, 0, 0]
    rotate(i[0]-1, i[1], rotated_flag)

print(sum([pow(2, ((i+1) * gears[i][0])) // 2 for i in range(4)]))

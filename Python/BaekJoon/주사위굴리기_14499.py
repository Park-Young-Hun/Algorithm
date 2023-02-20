import sys

n, m, row, col, k = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cmds = list(map(int, sys.stdin.readline().split()))


class Dice:
    def __init__(self, up, down, left, right, top, bottom):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def move(self, way):
        if way == 1:
            self.move_right()
        elif way == 2:
            self.move_left()
        elif way == 3:
            self.move_up()
        else:
            self.move_down()

    def move_up(self):
        temp_top = self.top
        self.top = self.down
        self.down = self.bottom
        self.bottom = self.up
        self.up = temp_top

    def move_down(self):
        temp_top = self.top
        self.top = self.up
        self.up = self.bottom
        self.bottom = self.down
        self.down = temp_top

    def move_left(self):
        temp_top = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = temp_top

    def move_right(self):
        temp_top = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = temp_top


def solution(n, m, row, col, k, table, cmds):
    dice = Dice(0, 0, 0, 0, 0, 0)
    delta_row = [0, 0, -1, 1]
    delta_col = [1, -1, 0, 0]

    for cmd in cmds:
        new_row = row + delta_row[cmd-1]
        new_col = col + delta_col[cmd-1]

        if 0 <= new_row < n and 0 <= new_col < m:
            row = new_row
            col = new_col

            dice.move(cmd)

            if table[row][col] == 0:
                table[row][col] = dice.bottom
            else:
                dice.bottom = table[row][col]
                table[row][col] = 0

            print(dice.top)


solution(n, m, row, col, k, table, cmds)

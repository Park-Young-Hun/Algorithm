import sys


class Dice:
    def __init__(self, up, down, left, right, top, bottom):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def move(self, way):
        if way == 0:
            self.move_right()
        elif way == 1:
            self.move_down()
        elif way == 2:
            self.move_left()
        else:
            self.move_up()

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


def solution(n, m, k, grid):
    dice = Dice(2, 5, 4, 3, 1, 6)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    direct = 0
    row, col = 0, 0

    while k > 0:
        delta_row, delta_col = delta[direct]
        dice.move(direct)


n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, m, k, grid))
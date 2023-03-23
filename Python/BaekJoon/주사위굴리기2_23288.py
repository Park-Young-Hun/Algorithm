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


def decide_direction(direction, bottom, target):
    if bottom > target:
        direction = (direction + 1) % 4
    elif bottom < target:
        direction -= 1
        if direction < 0:
            direction += 4
    return direction


def calc_score(target: int, pos: tuple):
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = [pos]
    visited[pos[0]][pos[1]] = True

    while stack:
        row, col = stack.pop()
        cnt += 1

        for i in range(4):
            delta_row, delta_col = delta[i]

            new_row = row + delta_row
            new_col = col + delta_col

            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:
                continue

            if not visited[new_row][new_col] and grid[new_row][new_col] == target:
                visited[new_row][new_col] = True
                stack.append((new_row, new_col))

    return cnt * target


def solution(n, m, k, grid):
    answer = 0
    direction = 0
    row, col = 0, 0
    dice = Dice(2, 5, 4, 3, 1, 6)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while k > 0:
        delta_row, delta_col = delta[direction]
        new_row = row + delta_row
        new_col = col + delta_col

        if new_row < 0 or new_row >= n or new_col < 0 or new_col >= m:  # 맵을 벗어나면 반대 방향으로 전환.
            direction = (direction + 2) % 4
            continue

        row = new_row
        col = new_col

        dice.move(direction)  # 주사위 이동.

        answer += calc_score(grid[row][col], (row, col))  # 점수 계산.

        direction = decide_direction(direction, dice.bottom, grid[row][col])  # 다음 방향 결정.
        k -= 1

    return answer


n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, m, k, grid))

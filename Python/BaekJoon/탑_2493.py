import sys


class Tower:
    def __init__(self, num, height):
        self.num = num
        self.height = height


def solution(n, towers):
    answers = [0] * n
    stack = []

    for i in range(n):
        towers[i] = Tower(i+1, towers[i])

    stack.append(towers[-1])

    for i in range(n-2, -1, -1):
        while stack and stack[-1].height < towers[i].height:
            tower = stack.pop()
            answers[tower.num - 1] = i+1

        stack.append(towers[i])
    return answers


n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

answers = solution(n, towers)

for answer in answers:
    print(answer, end=" ")

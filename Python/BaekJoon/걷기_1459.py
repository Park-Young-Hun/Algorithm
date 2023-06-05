import sys


def solution(x, y, w, s):
    answer = []

    answer.append(min(x, y) * s + abs(x - y) * w)

    if (x + y) % 2 == 0:
        answer.append(max(x, y) * s)
    else:
        answer.append((max(x, y) - 1) * s + w)

    answer.append((x + y) * w)

    return min(answer)


x, y, w, s = map(int, sys.stdin.readline().split())
print(solution(x, y, w, s))

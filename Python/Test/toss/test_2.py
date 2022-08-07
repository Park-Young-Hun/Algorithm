from collections import deque

def solution(levels):
    n = len(levels)
    levels.sort()
    target = deque()

    for i in range(n-1, -1, -1):
        target.append(levels[i])
        percent = len(target) / n

        if percent > 0.25:
            target.pop()
            break
    if target:
        return target.pop()
    else:
        return -1

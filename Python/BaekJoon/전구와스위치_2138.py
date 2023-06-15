import sys


def change(cur, target):
    press = 0

    for i in range(1, n):
        if cur[i - 1] == target[i - 1]:
            continue

        press += 1

        for j in range(i - 1, i + 2):
            if j < n:
                cur[j] = 1 - cur[j]

    if cur == target:
        return press

    return -1


def solution(n, bulbs, target):
    result_first_off = change(bulbs[:], target)

    bulbs[0] = 1 - bulbs[0]
    bulbs[1] = 1 - bulbs[1]

    result_first_on = change(bulbs, target)

    if result_first_on >= 0:
        result_first_on += 1

    if result_first_on >= 0 and result_first_off >= 0:
        return min(result_first_on, result_first_off)
    else:
        return max(result_first_on, result_first_off)


n = int(sys.stdin.readline())
bulbs = list(map(int, list(sys.stdin.readline().rstrip())))
target = list(map(int, list(sys.stdin.readline().rstrip())))
print(solution(n, bulbs, target))

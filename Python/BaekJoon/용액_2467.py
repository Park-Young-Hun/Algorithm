import sys
from bisect import bisect_left


def solve(n, solutions):
    answer = []
    alkali = []
    acid = []

    for solution in solutions:
        if solution < 0:
            alkali.append(solution)
        else:
            acid.append(solution)

    if len(alkali) > 1:
        answer.append((alkali[-1], alkali[-2]))
    if len(acid) > 1:
        answer.append((acid[0], acid[1]))

    if len(alkali) > len(acid):
        insert, target = acid, alkali
    else:
        insert, target = alkali, acid

    for num in insert:
        idx = bisect_left(target, -num)

        if idx == 0:
            answer.append((num, target[idx]))
            continue
        elif idx == len(target):
            answer.append((num, target[idx-1]))
            continue

        left_sub = abs(num + target[idx-1])
        right_sub = abs(num + target[idx])

        if left_sub < right_sub:
            answer.append((num, target[idx-1]))
        else:
            answer.append((num, target[idx]))

    answer.sort(key=lambda x: abs(x[0]+x[1]))
    return sorted(answer[0])


n = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))

print(*solve(n, solutions))

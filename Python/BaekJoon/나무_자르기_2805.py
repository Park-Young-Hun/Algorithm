import sys


def solution(n, need, trees):
    left = 0
    right = max(trees)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0

        for tree in trees:
            if tree > mid:
                cnt += tree - mid

        if cnt < need:
            right = mid - 1
        elif cnt > need:
            left = mid + 1
        else:
            return mid
    return right


first_line = list(map(int, sys.stdin.readline().split()))
second_line = list(map(int, sys.stdin.readline().split()))

print(solution(first_line[0], first_line[1], second_line))

import sys


def solution(n, boxes):
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if boxes[j] < boxes[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


n = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))
print(solution(n, boxes))


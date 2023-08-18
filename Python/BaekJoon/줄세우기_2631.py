import sys


def solution(n, children):
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if children[j] < children[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)


n = int(sys.stdin.readline())
children = [int(sys.stdin.readline()) for _ in range(n)]
print(solution(n, children))

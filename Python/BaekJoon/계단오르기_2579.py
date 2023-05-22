import sys


def solution(n, stairs):
    if n < 3:
        return sum(stairs)

    dp = [0] * n
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    return dp[n-1]


n = int(sys.stdin.readline())
stairs = [int(sys.stdin.readline()) for _ in range(n)]
print(solution(n, stairs))

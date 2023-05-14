import sys


def solution(n):
    dp = [0 for _ in range(n+2)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2

    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

    return dp[n] % 10007


n = int(sys.stdin.readline())
print(solution(n))

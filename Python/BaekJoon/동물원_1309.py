import sys


def solution(n):
    dp = [1] * (n+1)
    dp[1] = 3

    for i in range(2, n+1):
        dp[i] = 2 * dp[i-1] + dp[i-2]
        dp[i] %= 9901

    return dp[n]


n = int(sys.stdin.readline())
print(solution(n))

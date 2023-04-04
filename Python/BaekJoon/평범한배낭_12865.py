import sys


def solution(n, k, stuffs):
    dp = [[0] * (k+1) for _ in range(n+1)]
    stuff = [(0, 0)]
    stuff.extend(stuffs)

    for i in range(1, n+1):
        weight, val = stuff[i]

        for j in range(1, k+1):
            if weight > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + val)
    return dp[n][k]


n, k = map(int, sys.stdin.readline().split())
stuffs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, k, stuffs))

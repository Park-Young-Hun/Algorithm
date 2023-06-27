import sys


def solution(n, grid):
    dp = [[0] * n for _ in range(n)]

    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if grid[i][j] <= 0:
                continue

            if j + grid[i][j] < n:
                dp[i][j + grid[i][j]] += dp[i][j]

            if i + grid[i][j] < n:
                dp[i + grid[i][j]][j] += dp[i][j]
    
    return dp[n-1][n-1]


n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, grid))


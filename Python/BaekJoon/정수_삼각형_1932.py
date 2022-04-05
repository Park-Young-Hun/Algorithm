import sys

n = int(sys.stdin.readline())

triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[triangle[0][0]]]

for i in range(1, n):
    temp = []
    for j in range(len(triangle[i])):
        if j == 0:
            temp.append(dp[i-1][j] + triangle[i][j])
        elif j == len(triangle[i]) - 1:
            temp.append(dp[i-1][j-1] + triangle[i][j])
        else:
            temp.append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
    dp.append(temp)

print(max(dp[n-1]))

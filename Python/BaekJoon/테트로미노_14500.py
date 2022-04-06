import sys

n, m = map(int, sys.stdin.readline().split())

table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = []

for i in range(n):
    for j in range(m):
        if j + 3 < m:  # 일자 모양 2종류
            answer.append(table[i][j] + table[i][j+1] + table[i][j+2] + table[i][j+3])
        if i + 3 < n:
            answer.append(table[i][j] + table[i+1][j] + table[i+2][j] + table[i+3][j])

        if i + 1 < n and j + 1 < m:  # 정사각형 모양 1종류
            answer.append(table[i][j] + table[i][j+1] + table[i+1][j] + table[i+1][j+1])

        if i + 2 < n and j + 1 < m:  # ㄴ자 모양 8종류
            answer.append(table[i][j] + table[i+1][j] + table[i+2][j] + table[i+2][j+1])
        if i + 2 < n and j - 1 >= 0:
            answer.append(table[i][j] + table[i+1][j] + table[i+2][j] + table[i+2][j-1])
        if i + 2 < n and j - 1 >= 0:
            answer.append(table[i][j] + table[i][j-1] + table[i+1][j-1] + table[i+2][j-1])
        if i + 2 < n and j + 1 < m:
            answer.append(table[i][j] + table[i][j+1] + table[i+1][j+1] + table[i+2][j+1])
        if i + 1 < n and j + 2 < m:
            answer.append(table[i][j] + table[i+1][j] + table[i+1][j+1] + table[i+1][j+2])
        if i + 1 < n and j - 2 >= 0:
            answer.append(table[i][j] + table[i+1][j] + table[i+1][j-1] + table[i+1][j-2])
        if i - 1 >= 0 and j + 2 < m:
            answer.append(table[i][j] + table[i-1][j] + table[i-1][j+1] + table[i-1][j+2])
        if i - 1 >= 0 and j - 2 >= 0:
            answer.append(table[i][j] + table[i-1][j] + table[i-1][j-1] + table[i-1][j-2])

        if i + 2 < n and j + 1 < m:  # 지그재그 모양 4종류
            answer.append(table[i][j] + table[i+1][j] + table[i+1][j+1] + table[i+2][j+1])
        if i + 2 < n and j - 1 >= 0:
            answer.append(table[i][j] + table[i+1][j] + table[i+1][j-1] + table[i+2][j-1])
        if i + 1 < n and j + 2 < m:
            answer.append(table[i][j] + table[i][j+1] + table[i+1][j+1] + table[i+1][j+2])
        if i - 1 >= 0 and j + 2 < m:
            answer.append(table[i][j] + table[i][j+1] + table[i-1][j+1] + table[i-1][j+2])

        if i - 1 >= 0 and j + 2 < m:  # ㅗ모양 4종류
            answer.append(table[i][j] + table[i][j+1] + table[i-1][j+1] + table[i][j+2])
        if i + 1 < n and j + 2 < m:
            answer.append(table[i][j] + table[i][j+1] + table[i+1][j+1] + table[i][j+2])
        if i + 2 < n and j + 1 < m:
            answer.append(table[i][j] + table[i+1][j] + table[i+1][j+1] + table[i+2][j])
        if i + 2 < n and j - 1 >= 0:
            answer.append(table[i][j] + table[i+1][j] + table[i+1][j-1] + table[i+2][j])

print(max(answer))


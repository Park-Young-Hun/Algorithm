import sys

n = int(sys.stdin.readline())

city_map = []
result = []
global cnt
cnt = 0

for _ in range(n):
    temp = list(sys.stdin.readline())
    temp.pop()
    city_map.append(temp)


def dfs(row, col):
    global cnt
    cnt += 1
    city_map[row][col] = '0'

    if row > 0 and city_map[row-1][col] == '1':
        dfs(row - 1, col)
    if row < n-1 and city_map[row+1][col] == '1':
        dfs(row + 1, col)
    if col > 0 and city_map[row][col-1] == '1':
        dfs(row, col - 1)
    if col < n-1 and city_map[row][col + 1] == '1':
        dfs(row, col + 1)

    return


for i in range(n):
    for j in range(n):
        if city_map[i][j] == '1':
            dfs(i, j)
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i)

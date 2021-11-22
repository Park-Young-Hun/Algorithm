import sys


def dfs(row, col, count):
    count += 1
    city_map[row][col] = '0'

    if row > 0 and city_map[row - 1][col] == '1':
        count = dfs(row - 1, col, count)
    if row < n - 1 and city_map[row + 1][col] == '1':
        count = dfs(row + 1, col, count)
    if col > 0 and city_map[row][col - 1] == '1':
        count = dfs(row, col - 1, count)
    if col < n - 1 and city_map[row][col + 1] == '1':
        count = dfs(row, col + 1, count)

    return count


n = int(sys.stdin.readline())

city_map = []
result = []

for _ in range(n):
    temp = list(sys.stdin.readline())
    temp.pop()
    city_map.append(temp)

for i in range(n):
    for j in range(n):
        if city_map[i][j] == '1':
            result.append(dfs(i, j, 0))

result.sort()
print(len(result))
for i in result:
    print(i)

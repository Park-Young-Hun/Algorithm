import sys


def zero_cnt(table):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == '0':
                cnt += 1
    return cnt


n, m = map(int, sys.stdin.readline().split())
office = [sys.stdin.readline().split() for _ in range(n)]
cameras = []

for i in range(n):
    for j in range(m):
        if office[i][j] == '1':
            cameras.append(['U', 'D', 'L', 'R'])
        elif office[i][j] == '2':
            cameras.append(['U', 'L'])
        elif office[i][j] == '3':
            cameras.append(['U', 'D', 'L', 'R'])
        elif office[i][j] == '4':
            cameras.append(['U', 'D', 'L', 'R'])
        elif office[i][j] == '5':
            cameras.append(['U'])

cases = []
print(cameras)
for i in cameras:
    for j in i:
        

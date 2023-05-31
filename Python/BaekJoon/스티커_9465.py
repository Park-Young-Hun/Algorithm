import sys


def solution(n, s):
    for j in range(1, n):
        if j == 1:
            s[0][j] += s[1][j - 1]
            s[1][j] += s[0][j - 1]
        else:
            s[0][j] += max(s[1][j - 1], s[1][j - 2])
            s[1][j] += max(s[0][j - 1], s[0][j - 2])
    return max(s[0][n-1], s[1][n-1])


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    stickers = []

    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    print(solution(n, stickers))

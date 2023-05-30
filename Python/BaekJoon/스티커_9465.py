import sys

def solution(n, stickers):
    

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    stickers = []

    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    print(solution(n, stickers))
import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]
print(board)

def dfs(path):

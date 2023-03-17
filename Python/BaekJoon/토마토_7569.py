import sys

n, m, h = map(int, sys.stdin.readline().split())
storage = []

for _ in range(h):
    storage.append([list(map(int, sys.stdin.readline().split())) for _ in range(m)])

print(storage)

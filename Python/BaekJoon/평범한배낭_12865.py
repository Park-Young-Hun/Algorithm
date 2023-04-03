import sys
from collections import defaultdict


def solution(n, k, stuffs):
    value = defaultdict(int)
    stuffs.sort(key=lambda x: (x[0], -x[1]))
    print(stuffs)

    for weight, val in stuffs:
        value[weight] = val


n, k = map(int, sys.stdin.readline().split())
stuffs = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, k, stuffs))

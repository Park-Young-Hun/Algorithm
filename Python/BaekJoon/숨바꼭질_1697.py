import sys
from collections import deque


def delta_x(x):
    return [2 * x, x + 1, x - 1]


def solution(n, k, max_x):
    time = 0
    visited = [False] * (max_x + 1)
    q = deque([n])

    while q:
        for _ in range(len(q)):
            cur = q.popleft()

            if cur == k:
                return time

            for new_x in delta_x(cur):
                if 0 <= new_x <= max_x and not visited[new_x]:
                    q.append(new_x)
                    visited[new_x] = True
        time += 1
    return -1


n, k = map(int, sys.stdin.readline().split())
print(solution(n, k, 100000))

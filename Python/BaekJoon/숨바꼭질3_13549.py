import sys
from collections import deque


def delta_x(x):
    return [2 * x, x - 1, x + 1]


def solution(n, k, max_x):
    visited = [False] * (max_x + 1)
    q = deque([(n, 0)])
    visited[n] = True

    while q:
        pos, time = q.popleft()

        if pos == k:
            return time

        for i in range(len(delta_x(pos))):
            new_x = delta_x(pos)

            if 0 <= new_x[i] <= max_x and not visited[new_x[i]]:
                visited[new_x[i]] = True

                if i == 0:
                    q.appendleft((new_x[i], time))
                else:
                    q.append((new_x[i], time + 1))


n, k = map(int, sys.stdin.readline().split())
print(solution(n, k, 100000))

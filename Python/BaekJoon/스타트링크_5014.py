import sys
from collections import deque


def solution(n, start, target, up, down):
    cnt = 0
    visited = [False] * (n+1)
    delta = [up, -down]
    q = deque([start])

    while q:
        for _ in range(len(q)):
            cur = q.popleft()

            if cur == target:
                return cnt

            for i in range(2):
                new_floor = cur + delta[i]

                if 0 < new_floor <= n and not visited[new_floor]:
                    visited[new_floor] = True
                    q.append(new_floor)
        cnt += 1
    return "use the stairs"


n, start, target, up, down = map(int, sys.stdin.readline().split())
print(solution(n, start, target, up, down))

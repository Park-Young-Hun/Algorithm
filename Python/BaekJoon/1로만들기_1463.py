import sys
from collections import deque


def solution(n):
    answer = 0
    q = deque([n])
    visited = [False] * n

    while q:
        for _ in range(len(q)):
            x = q.popleft()

            if x == 1:
                return answer

            new_x = [x // 3, x // 2, x - 1]

            for i in range(len(new_x)):
                if i == 0 and x % 3 != 0:
                    continue
                if i == 1 and x % 2 != 0:
                    continue

                if not visited[new_x[i]]:
                    visited[new_x[i]] = True
                    q.append(new_x[i])
        answer += 1


n = int(sys.stdin.readline())
print(solution(n))

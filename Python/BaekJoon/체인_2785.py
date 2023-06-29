import sys
from collections import deque


def solution(n, chains):
    answer = 0
    chains.sort()
    q = deque(chains)

    while len(q) > 1:
        min_chain = q.popleft()

        while len(q) > 1 and min_chain > 0:
            q.append(q.pop() + q.pop())
            min_chain -= 1
            answer += 1

        if min_chain > 0:
            answer += 1

    return answer


n = int(sys.stdin.readline())
chains = list(map(int, sys.stdin.readline().split()))
print(solution(n, chains))

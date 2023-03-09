import sys
from collections import defaultdict, deque


def solution(graph, n, start, target):
    breadth = 0
    visited = [False] * (n + 1)

    q = deque([start])
    visited[start] = True

    while q:
        for _ in range(len(q)):
            node = q.popleft()

            if node == target:
                return breadth

            for next_node in graph[node]:
                if not visited[next_node]:
                    q.append(next_node)
                    visited[next_node] = True
        breadth += 1
    return -1


n = int(sys.stdin.readline())
start, target = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = defaultdict(list)

for _ in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)

print(solution(graph, n, start, target))

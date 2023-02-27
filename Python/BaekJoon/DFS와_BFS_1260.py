import sys
from collections import defaultdict, deque


def dfs(start, graph):
    answer = []
    visited = [False] * (N + 1)
    stack = [start]

    while stack:
        node = stack.pop()

        if not visited[node]:
            answer.append(node)
            visited[node] = True

        for next_node in sorted(graph[node], reverse=True):
            if not visited[next_node]:
                stack.append(next_node)

    return answer


def bfs(start, graph):
    answer = []
    visited = [False] * (N + 1)
    q = deque([start])
    visited[start] = True

    while q:
        node = q.popleft()
        answer.append(node)

        for next_node in sorted(graph[node]):
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
    return answer


def solution(N, M, start, graph):

    for node in dfs(start, graph):
        print(node, end=" ")

    print()

    for node in bfs(start, graph):
        print(node, end=" ")


N, M, start = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

solution(N, M, start, graph)

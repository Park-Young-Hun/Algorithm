import sys
import heapq
from collections import defaultdict


def dijkstra(start, graph):
    q = []
    distance = [INF] * (n + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cur_dist, cur = heapq.heappop(q)

        if distance[cur] < cur_dist:
            continue

        for dest_dist, dest in graph[cur]:
            new_dist = cur_dist + dest_dist

            if new_dist < distance[dest]:
                distance[dest] = new_dist
                heapq.heappush(q, (new_dist, dest))
    return distance


def solution(n, m, x):
    answer = []
    graph_go = defaultdict(list)
    graph_back = defaultdict(list)

    for _ in range(m):
        start, end, t = map(int, sys.stdin.readline().split())
        graph_go[end].append((t, start))
        graph_back[start].append((t, end))

    distance_go = dijkstra(x, graph_go)
    distance_back = dijkstra(x, graph_back)

    for i in range(1, n+1):
        answer.append(distance_go[i] + distance_back[i])

    return max(answer)


INF = int(1e9)
n, m, x = map(int, sys.stdin.readline().split())
print(solution(n, m, x))

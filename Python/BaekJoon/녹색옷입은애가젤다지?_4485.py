import sys
import heapq
from collections import defaultdict, deque


def make_graph(cave):
    n = len(cave)
    start = (0, 0)
    q = deque([start])
    graph = defaultdict(list)
    delta = [(1, 0), (0, 1)]

    while q:
        row, col = q.popleft()

        for i in range(len(delta)):
            delta_row, delta_col = delta[i]
            new_row = row + delta_row
            new_col = col + delta_col

            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n:
                continue

            graph[(row, col)].append((cave[new_row][new_col], (new_row, new_col)))
            q.append((new_row, new_col))
    return graph


def solution(n, cave):
    graph = make_graph(cave)
    distance = [[int(1e9)] * n for _ in range(n)]
    distance[0][0] = 0
    priority_queue = []
    print(graph)

    heapq.heappush(priority_queue, (0, (0, 0)))

    while priority_queue:
        dist, cur = heapq.heappop(priority_queue)
        print(cur)
        if distance[cur[0]][cur[1]] < dist:
            continue

        for new_dist, next_node in graph[cur]:
            if dist + new_dist < distance[next_node[0]][next_node[1]]:
                distance[next_node[0]][next_node[1]] = dist + new_dist
                heapq.heappush(priority_queue, next_node)
    print(distance)





n = int(sys.stdin.readline())

while n != 0:
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(solution(n, cave))
    n = int(sys.stdin.readline())

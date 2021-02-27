import sys


def dfs(graph, start_node):
    visited = list()
    need_visit = list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return len(visited)-1


graph = dict()
vertex_num = int(sys.stdin.readline())

for i in range(1, vertex_num+1):
    graph[i] = list()

edge_num = int(sys.stdin.readline())

for i in range(edge_num):
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

print(dfs(graph, 1))




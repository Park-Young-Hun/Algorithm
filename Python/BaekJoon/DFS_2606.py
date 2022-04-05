import sys


def dfs(graph, start_node):  # DFS 탐색 알고리즘.
    visited = list()  # 탐색한 노드 (큐)
    need_visit = list()  # 탐색해야할 노드 (스택)
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:  # 이미 간곳이 아니면 탐색하고 연결된 모든 노드들을 스택에 넣는다.
            visited.append(node)
            need_visit.extend(graph[node])

    return len(visited)-1


graph = dict()
vertex_num = int(sys.stdin.readline())

for i in range(1, vertex_num+1):  # 입력받은 컴퓨터 수 만큼 vertex 생성.
    graph[i] = list()

edge_num = int(sys.stdin.readline())

for i in range(edge_num):  # 입력받은 edge 수 만큼 연결 관계를 표현
    key, value = map(int, sys.stdin.readline().split())
    graph[key].append(value)
    graph[value].append(key)

print(dfs(graph, 1))




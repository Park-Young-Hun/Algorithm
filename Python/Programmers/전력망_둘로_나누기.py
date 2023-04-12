from collections import defaultdict


def dfs(cur, cnt):
    global visited
    visited[cur] = True
    cnt += 1

    for node in graph[cur]:
        if not visited[node] and is_connect[cur][node]:
            cnt = dfs(node, cnt)
    return cnt


def solution(n, wires):
    answer = int(1e9)

    global visited
    global graph
    global is_connect

    graph = defaultdict(list)
    is_connect = [[False] * (n + 1) for _ in range(n + 1)]

    for start, end in wires:
        graph[start].append(end)
        graph[end].append(start)
        is_connect[start][end] = True
        is_connect[end][start] = True

    for start, end in wires:
        visited = [False] * (n + 1)

        is_connect[start][end] = False
        is_connect[end][start] = False

        result = abs(dfs(start, 0) - dfs(end, 0))

        if answer > result:
            answer = result

        is_connect[start][end] = True
        is_connect[end][start] = True

    return answer

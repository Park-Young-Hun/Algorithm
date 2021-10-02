from collections import defaultdict


def solution(n, edge):
    graph = defaultdict(list)

    for e in edge:  # graph를 dict 형태로 표현.
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    return bfs(graph, 1)


def bfs(graph, root):
    breadth = []  # breadth를 관리.
    visited = set([])
    cnt = 0  # 현재 breadth의 node 갯수.

    breadth.append(root)
    visited.add(root)

    while breadth:  # breadth가 None이면 탐색을 끝까지 했다는 뜻.
        cnt = len(breadth)

        for node in breadth[:]:
            children = list(set(graph[node]) - visited)  # 방문안한 각 node들의 자식 node들.
            breadth.extend(children)  # 다음 breadth에 속하는 node들 추가.
            for child in children:  # 방문 처리.
                visited.add(child)
            breadth.remove(node)  # 이전 breadth에 속하는 node들 제거.

    return cnt  # 마지막 breadth node 갯수 반환.

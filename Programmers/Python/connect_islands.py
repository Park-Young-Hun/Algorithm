def solution(n, costs):  # kruskal 알고리즘

    islands = [i for i in range(n)]
    edges = 0
    min_cost = 0

    costs.sort(key=lambda x: x[2])  # edge의 weight 기준으로 오름차순 정렬.

    while edges != n - 1:
        cost = costs.pop(0)
        if find_root(islands, cost[0]) != find_root(islands, cost[1]):  # cycle 이루는지 체크.
            union_node(islands, cost[0], cost[1])
            edges += 1
            min_cost += cost[2]

    return min_cost


def find_root(root_nodes, node):  # 경로 압축
    if root_nodes[node] != node:
        root_nodes[node] = find_root(root_nodes, root_nodes[node])
    return root_nodes[node]


def union_node(root_nodes, a, b):  # 두 vertex 이어주기.
    a = find_root(root_nodes, a)
    b = find_root(root_nodes, b)

    root_nodes[b] = a


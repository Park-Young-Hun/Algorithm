def solution(n, computers):
    answer = 1
    universal_set = set([i for i in range(n)])  # 전체 vertex 집합.
    visited = set()  # 방문한 vertex.

    visited = dfs(computers, 0, visited)  # 0번 vertex부터 첫번째 트리 탐색.

    while True:
        if universal_set != visited:  # 다 방문하지 않았으면
            target = list(universal_set - visited)  # 방문하지 않은 vertex를 시작으로
            visited = dfs(computers, target[0], visited)  # dfs 탐색.
            answer += 1  # 트리 추가(네트워크 추가)
        else:
            break

    return answer


def dfs(computers, vertex, visited):
    for i in range(len(computers[vertex])):  # 하나의 vertex에 대하여 순회하면서
        visited.add(vertex)  # 방문 체크.
        if i not in list(visited) and computers[vertex][i] == 1:  # 방문하지 않았는데 1로 표기되어있다면(연결되어있다면)
            visited = dfs(computers, i, visited)  # 해당 vertex에서 재귀 탐색.

    return visited

from collections import defaultdict


def solution(n, results):
    answer = 0

    graph = defaultdict(list)
    for result in results:  # graph dictionary는 "선수 번호" : [해당 선수가 이긴 result들] 로 구성되어 있다.
        graph[result[0]].append(result)

    for key in range(1, n + 1):  # 삼단논법을 통해 확장시킬 수 있는 result들을 확장시킨다.
        index = 0
        while True:
            if graph[key]:  # 해당 선수가 이긴 결과가 있으면
                graph = syllogism(graph, graph[key][index])  # 삼단논법을 통해 확장시킨다.
                if len(graph[key]) == index + 1:  # 더이상 확장 시킬게 없으면 담은 선수 번호로 넘어간다.
                    break
                else:  # 확장시켰으면 그 result에 대해서도 삼단논법을 적용해 확장시킨다.
                    index += 1
            else:  # 해당 선수가 이긴 결과가 없으면 넘어감.
                break

    cnt = [0] * n
    for key in graph.keys():  # graph을 순회하면서 result에서 각각 몇번 등장하는지 count (각 vertex의 edge 수)
        for i in graph[key]:
            cnt[i[0] - 1] += 1
            cnt[i[1] - 1] += 1

    for i in cnt:  # edge가 n-1개이면 정답에 포함.
        if i >= n - 1:
            answer += 1

    return answer


def syllogism(graph, result):  # 삼단논법을 통해 만든 결과들을 추가해주는 함수.
    for i in graph[result[1]]:
        if [result[0], i[1]] not in graph[result[0]]:
            graph[result[0]].append([result[0], i[1]])

    return graph

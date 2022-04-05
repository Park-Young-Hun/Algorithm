from collections import deque


def solution(begin, target, words):
    breadth = 0  # 그래프에서 몇번째 breadth에 속하는지.
    queue = deque()  # 방문할 노드
    visited = set([])  # 방문한 노드
    same_breadth = []  # 같은 breadth에 속하는 노드들을 한번에 queue에서 제거후 보관.

    if target not in words:
        return 0

    queue.append(begin)
    visited.add(begin)

    while queue:
        while queue:  # 같은 breadth에 속하는 노드들을 한번에 queue에서 제거 후 보관.
            same_breadth.append(queue.popleft())
        breadth += 1  # 한번에 queue에서 제거할때 다음 breadth를 탐색.
        for begin in same_breadth:
            words = list(set(words) - visited)  # 방문 안한 노드.

            for word in words:
                count = 0
                for i in range(len(begin)):

                    if begin[i] != word[i]:
                        count += 1

                if count == 1:
                    if word == target:
                        return breadth
                    queue.append(word)
                    visited.add(word)
    return 0

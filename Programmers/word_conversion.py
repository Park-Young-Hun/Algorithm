from collections import deque


def solution(begin, target, words):
    answer = 0
    visited = set([])
    queue = deque()
    queue.append(begin)

    if target not in words:
        return answer

    for word in words:
        for i in range(len(begin)):
            count = 0

            if begin[i] != word[i]:
                count += 1

        if count == 1:
            answer += 1
            queue.append(word)

            if begin == target:
                return answer
    queue.popleft()

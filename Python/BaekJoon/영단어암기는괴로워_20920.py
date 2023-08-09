import sys
from collections import Counter


def solution(m, words):
    note = []
    answer = []

    for word in words:
        if len(word) >= m:
            note.append(word)

    note = list(Counter(note).items())
    note.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

    for word, cnt in note:
        answer.append(word)

    return answer


n, m = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
answers = solution(m, words)

for answer in answers:
    print(answer)

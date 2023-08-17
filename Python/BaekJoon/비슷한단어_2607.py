import sys
from collections import defaultdict


def is_similar(target, word):
    answer = 0
    chr_cnts = defaultdict(int)

    for char in target:
        chr_cnts[char] += 1

    for char in word:
        if chr_cnts[char] > 0:
            chr_cnts[char] -= 1

    if sum(chr_cnts.values()) == 1 or sum(chr_cnts.values()) == 0:
        answer += 1

    return answer


def solution(n, words):
    answer = 0
    target = words.pop(0)
    s = len(target)

    for word in words:
        if len(word) == s:
            answer += is_similar(target, word)
        elif len(word) == s-1:
            answer += is_similar(target, word)
        elif len(word) == s+1:
            answer += is_similar(word, target)
    return answer


n = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
print(solution(n, words))

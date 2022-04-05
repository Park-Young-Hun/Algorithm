from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        combination_arr = []
        for order in orders:
            combination_arr += list(combinations(sorted(order), c))
        combination_arr = Counter(combination_arr)
        answer += [''.join(k) for k, v in combination_arr.items() if v == max(combination_arr.values()) and v > 1]

    return sorted(answer)

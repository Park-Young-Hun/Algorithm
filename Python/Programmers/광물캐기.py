import math
from itertools import product
from copy import deepcopy


def solution(picks, minerals):
    answer = int(2e9)
    pick_kinds = [0, 1, 2]

    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            minerals[i] = 0
        elif minerals[i] == "iron":
            minerals[i] = 1
        elif minerals[i] == "stone":
            minerals[i] = 2

    cases = list(product(pick_kinds, repeat=min(math.ceil(len(minerals) / 5), sum(picks))))

    for case in cases:
        fatigue = 0
        temp_picks = deepcopy(picks)

        for i in range(len(case)):
            temp_picks[case[i]] -= 1

            if temp_picks[case[i]] < 0:
                fatigue = 0
                break

            start = i * 5
            end = min(start + 5, len(minerals))

            for j in range(start, end):
                diff = case[i] - minerals[j]

                if diff < 0:
                    diff = 0

                fatigue += pow(5, diff)

        if 0 < fatigue < answer:
            answer = fatigue

    return answer

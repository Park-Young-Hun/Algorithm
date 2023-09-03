from itertools import permutations


def solution(ability):
    answer = 0

    cases = list(permutations(ability, len(ability[0])))

    for case in cases:
        class_ability = 0

        for i in range(len(ability[0])):
            class_ability += case[i][i]

        if class_ability > answer:
            answer = class_ability

    return answer

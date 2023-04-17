from collections import defaultdict


def solution(survey, choices):
    answer = ''
    result = defaultdict(int)
    groups = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    score = [0, 3, 2, 1, 0, 1, 2, 3]

    for i in range(len(survey)):
        left, right = list(survey[i])

        if choices[i] > 4:
            result[right] += score[choices[i]]
        else:
            result[left] += score[choices[i]]

    for left, right in groups:
        if result[left] > result[right]:
            answer += left
        elif result[left] < result[right]:
            answer += right
        else:
            answer += min(left, right)

    return answer

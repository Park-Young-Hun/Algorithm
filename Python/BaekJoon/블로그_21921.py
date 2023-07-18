import sys


def solution(n, x, visitors):
    temp_answers = []
    sum_visitors = sum(visitors[:x])
    max_sum = sum_visitors
    temp_answers.append(max_sum)

    for i in range(len(visitors) - x):
        sum_visitors -= visitors[i]
        sum_visitors += visitors[i+x]

        if sum_visitors >= max_sum:
            temp_answers.append(sum_visitors)
            max_sum = sum_visitors

    answers = []

    for answer in temp_answers:
        if answer == max_sum and answer != 0:
            answers.append(answer)

    if not answers:
        return "SAD"

    return str(max_sum) + "\n" + str(len(answers))


n, x = map(int, sys.stdin.readline().split())
visitors = list(map(int, sys.stdin.readline().split()))
print(solution(n, x, visitors))

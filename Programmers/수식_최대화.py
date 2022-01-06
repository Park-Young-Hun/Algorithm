from itertools import permutations


def solution(expression):
    answer = 0
    operators = ["+", "*", "-"]
    cases = list(permutations(operators, 3))

    print(cases)

    return answer

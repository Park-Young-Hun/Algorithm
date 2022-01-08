from itertools import permutations


def solution(expression):
    answer = 0
    operators = ["+", "*", "-"]
    cases = list(permutations(operators, 3))

    print(cases)

    for case in cases:
        for operator in case:
            temp = ""
            for letter in expression:
                temp += letter

    return answer

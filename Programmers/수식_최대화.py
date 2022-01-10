from itertools import permutations


def solution(expression):
    answer = []
    operators = ["+", "*", "-"]

    cases = list(permutations(operators, 3))

    for case in cases:
        temp_expression = expression
        for operator in case:
            target = ""
            calc_fg = False
            for i in temp_expression[:]:

                if i in operators and len(target) > 0:

                    if calc_fg and target[-1] not in operators:
                        temp_expression = temp_expression.replace(target, str(eval(target)))
                        target = str(eval(target))
                        calc_fg = False

                    if i == operator:
                        target += i
                        calc_fg = True
                    elif target[-1] in operators:
                        target += i
                    else:
                        target = ""
                else:
                    target += i

            if calc_fg:
                temp_expression = temp_expression.replace(target, str(eval(target)))
        answer.append(abs(int(temp_expression)))

    return max(answer)

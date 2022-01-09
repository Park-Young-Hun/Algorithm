from itertools import permutations


def solution(expression):
    answer = 0
    operators = ["+", "*", "-"]

    cases = list(permutations(operators, 3))

    for case in cases:
        temp_expression = expression
        for operator in case:
            target = ""
            calc_fg = False
            for i in temp_expression[:]:
                #print("target", target)
                if i in operators and len(target) > 0:

                    if calc_fg:
                        print(temp_expression)
                        temp_expression = temp_expression.replace(target, str(eval(target)))
                        print(temp_expression)
                        target = str(eval(target))
                        calc_fg = False
                    if i == operator:
                        target += i
                        calc_fg = True
                    else:
                        target = ""
                else:
                    target += i

        # print(temp_expression)

    return answer


solution("100-200*300-500+20")

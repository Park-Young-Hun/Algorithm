from itertools import permutations


def solution(expression):
    answer = []
    operators = ["+", "*", "-"]

    cases = list(permutations(operators, 3))  # 3!의 경우의 수.

    for case in cases:
        temp_expression = expression
        for operator in case:  # operator를 하나씩 적용.
            target = ""
            calc_fg = False  # 현재 계산할 operator가 target에 들어올 경우 True
            for i in temp_expression[:]:
                if i in operators and len(target) > 0:  # i가 연산자이고 왼쪽 피연산자가 있으면

                    if calc_fg and target[-1] not in operators:  # 계산할 준비가 됐고, 오른쪽 피연산자가 있으면 계산.
                        temp_expression = temp_expression.replace(target, str(eval(target)))
                        target = str(eval(target))
                        calc_fg = False

                    if i == operator:  # i가 현재 우선순위에 있는 연산자라면 target에 넣어주고 계산 준비 완료 flag on.
                        target += i
                        calc_fg = True
                    elif target[-1] in operators:  # 연산자가 연달아온 경우 -인 unary operator이기 때문에 target에 저장.
                        target += i
                    else:  # 우선순위에 없는 연산자가 오면 target 초기화.
                        target = ""
                else:  # 숫자가 온 경우 target에 추가.
                    target += i

            if calc_fg:  # expression 탐색이 끝날때 계산 준비가 되어 있으면 계산해준다.
                temp_expression = temp_expression.replace(target, str(eval(target)))
        answer.append(abs(int(temp_expression)))

    return max(answer)

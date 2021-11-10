def solution(p):
    if p == "":
        return ""

    if verify(p):  # 올바른 괄호 문자열이면 그대로 return.
        return p

    p = list(p)
    u = [p.pop(0)]
    cnt = 1

    while cnt != 0:  # 균형잡힌 괄호 문자열을 p로부터 분리.
        item = p.pop(0)

        if item == u[0]:
            u.append(item)
            cnt += 1
        else:
            u.append(item)
            cnt -= 1

    if verify(u):  # u가 올바른 괄호 문자열일 경우.
        return "".join(u) + solution("".join(p))
    else:  # u가 올바른 괄호 문자열이 아닌 경우.
        u.pop(0)
        u.pop()

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        return '(' + solution("".join(p)) + ')' + "".join(u)


def verify(s):  # 올바른 괄호 문자열인지 판단.
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop(0)
            else:
                return False
    return True

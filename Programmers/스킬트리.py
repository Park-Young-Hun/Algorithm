def solution(skill, skill_trees):
    answer = 0
    n = len(skill)

    for i in skill_trees:
        check = [0] * n
        error = False

        for j in i:
            if j in skill:
                idx = skill.index(j)
                if idx != 0 and check[idx - 1] == 0:
                    error = True
                    break
                else:
                    check[idx] = 1
        if not error:
            answer += 1

    return answer

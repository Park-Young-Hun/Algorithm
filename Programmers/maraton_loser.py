def solution(participant, completion):
    answer = ''
    p_dic = {}
    c_dic = {}
    p_set = set(participant)

    for p in participant:
        if p in p_dic:
            p_dic[p] += 1
        else:
            p_dic[p] = 1

    for c in completion:
        if c in c_dic:
            c_dic[c] += 1
        else:
            c_dic[c] = 1

    for p in p_set:
        if p in c_dic:
            p_dic[p] -= c_dic[p]

    for p in p_set:
        if p_dic[p] == 1:
            answer = p

    return answer

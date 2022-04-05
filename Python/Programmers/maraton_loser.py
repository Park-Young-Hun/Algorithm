def solution(participant, completion):
    answer = ''
    p_dic = {}  # 참가자 딕셔너리
    c_dic = {}  # 완주자 딕셔너리
    p_set = set(participant)  # 중복을 제거한 참가자 집합

    for p in participant:  # {이름 : 참가자 리스트에 존재하는 이름 빈도 수}
        if p in p_dic:
            p_dic[p] += 1
        else:
            p_dic[p] = 1

    for c in completion:  # {이름 : 완주자 리스트에 존재하는 이름 빈도 수}
        if c in c_dic:
            c_dic[c] += 1
        else:
            c_dic[c] = 1

    for p in p_set:  # 같은 이름일 경우 (참가자 리스트에 존재하는 이름 빈도 수 - 완주자 리스트에 존재하는 이름 빈도 수)
        if p in c_dic:
            p_dic[p] -= c_dic[p]

    for p in p_set:  # 이름 빈도 수가 1인 이름(키값)이 완주 실패자.
        if p_dic[p] == 1:
            answer = p

    return answer

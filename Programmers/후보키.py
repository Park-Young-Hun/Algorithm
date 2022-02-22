from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])
    index_list = [i for i in range(col)]  # index는 속성값의 위치.
    index_combo = []  # index들의 모든 조합.
    candidate_key = []  # 최종 선택된 후보키 모음.

    for i in range(col):
        index_combo += list(combinations(index_list, i + 1))

    for case in index_combo:  # 하나의 속성 묶음에 대하여
        is_minimal = True
        is_unique = True

        for key in candidate_key:  # 먼저 최소성을 만족하는지 검사.
            if not set(key) - set(case):  # case에 후보키가 이미 포함되어 있다면
                is_minimal = False  # 최소성 불만족.
                break

        if is_minimal:  # 최소성을 만족한다면
            for i in range(row):  # 같은 row가 있는지 검사.
                for j in range(i + 1, row):
                    target_i = [relation[i][k] for k in case]
                    target_j = [relation[j][k] for k in case]

                    if target_i == target_j:  # 같은 row가 있으면
                        is_unique = False  # 유일성 불만족.
                        break
                if not is_unique:
                    break

            if is_unique:  # 유일성을 만족한다면
                candidate_key.append(case)  # 후보키 리스트에 추가.

    return len(candidate_key)

def solution(clothes):
    answer = 1

    closet = {}

    for cloth in clothes:
        if cloth[1] not in closet:
            closet[cloth[1]] = []

        closet[cloth[1]].append(cloth[0])

    key_list = list(closet.keys())

    for i in key_list:
        answer *= len(closet[
                          i]) + 1  # 투명색 옷이 있다고 가정하여 각각의 옷의 종류에 옷을 하나씩 추가함으로써 모든 종류의 옷을 다 선택해야 되게 한다. 즉, 각각의 경우의 수들을 그냥 곱해주면 된다.

    return answer - 1  # 모든 옷의 종류가 투명색 옷인 경우는 제외한다.
def solution(genres, plays):
    answer = []
    dic_genres = {}
    dic_sum = {}
    selected_genres = []

    for i in range(len(genres)):  # {장르:고유번호 리스트} 형태로 딕셔너리 구성.
        if genres[i] not in dic_genres:
            dic_genres[genres[i]] = []
            dic_genres[genres[i]].append(i)
        else:
            dic_genres[genres[i]].append(i)

    key_list = list(dic_genres.keys())

    for key in key_list:  # {장르:장르별 총 재생횟수} 형태로 딕셔너리 구성.
        dic_sum[key] = 0

        for i in range(len(dic_genres[key])):
            dic_sum[key] += plays[dic_genres[key][i]]

    sum_list = list(dic_sum.values())
    sum_list.sort(reverse=True)  # 총 재생횟수 리스트 내림차순 정렬.

    for i in range(len(sum_list)):  # 재생횟수가 많은 순서대로 장르를 selected-genres에 삽입.
        for key in key_list:
            if dic_sum[key] == sum_list[i]:
                selected_genres.append(key)

    for k in selected_genres:  # 각 장르내에서 재생횟수가 높은 상위 2개를 선택하여 앨범에 수록.
        for j in range(2):
            if len(dic_genres[k]) == 0:  # 장르에 노래가 하나만 있는 경우 예외처리.
                break
            max_play = dic_genres[k][0]
            for i in range(len(dic_genres[k])):
                if plays[dic_genres[k][i]] > plays[max_play]:
                    max_play = dic_genres[k][i]

            answer.append(max_play)
            dic_genres[k].remove(max_play)

    return answer

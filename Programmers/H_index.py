def solution(citations):
    answer = 0
    select = []
    index = 0

    citations.sort(reverse=True)  # 내림차순으로 정렬.

    point = citations[0]  # 기준점 Init.

    while point >= 0:  # 기준점이 음수가 아닐때까지 감소시키며 진행.
        if point <= index + 1:  # 기준점보다 큰 요소들의 갯수 = 현재까지 index까지의 요소 갯수 = index+1
            select.append(point)  # 조건을 만족시키는 것들 보관.

        if index != len(citations) - 1:
            if point == citations[index + 1]:  # 기준점이 다음 index에 도달하면 index를 증가시켜준다.
                index += 1
            else:  # index 사이를 기준점이 이동하면서 체크.
                point -= 1
        else:  # index가 더이상 움직일 수 없더라도 기준점은 계속 움직인다.
            point -= 1

    answer = max(select)
    return answer

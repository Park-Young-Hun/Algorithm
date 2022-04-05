def solution(routes):
    answer = 1

    routes.sort(key=lambda x: x[1])  # 차를 나간순서대로 정렬.
    camera = routes[0][1]  # 카메라를 차가 가장 먼저 나간 지점에 배치.

    for i in routes:
        if camera < i[0]:  # 현재 카메라 지점 이후에 들어온 차량이 있으면
            camera = i[1]  # 그 차량이 나간 지점에 카메라 배치.
            answer += 1

    return answer

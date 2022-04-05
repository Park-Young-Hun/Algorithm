def solution(people, limit):
    answer = 0
    heavy = len(people) - 1
    light = 0

    people.sort()

    while heavy != light:  # 맨 뒤부터 시작하는 index와 맨 앞에서부터 시작한 index가 같아질때까지
        if people[heavy] + people[light] <= limit:  # 가장 무거운 사람과 가장 가벼운 사람을 같이 태울 수 있으면
            people[heavy] += people[light]  # 같이 태운다.
            light += 1  # 그 다음 가벼운 사람도 태울 수 있는지 체크.
        else:  # 베에 가장 가벼운 사람도 못태운다면 더이상 아무도 태우지 못하기 때문에
            answer += 1  # 배를 출발 시키고
            heavy -= 1  # 그 다음 무거운 사람을 새로운 배에 태운다.

    answer += 1  # 마지막 사람(들)이 타는 배 출발.

    return answer
# 34mins

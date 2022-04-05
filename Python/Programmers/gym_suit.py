def solution(n, lost, reserve):
    answer = 0

    new_lost = list(set(lost) - set(reserve))  # 여분 가져왔는데 도난 당한 사람은 두 리스트에서 모두 제거.
    new_reserve = list(set(reserve) - set(lost))

    answer += n  # 일단 전체 학생수로 초기화.

    for i in new_lost:
        if i > 1 and i - 1 in new_reserve:  # 앞번호 사람한테 빌릴 수 있으면 차감하지 않음.
            new_reserve.remove(i - 1)
            continue

        if i < n and i + 1 in new_reserve:  # 뒷번호 사람한테 빌릴 수 있으면 차감하지 않음.
            new_reserve.remove(i + 1)
            continue

        answer -= 1  # 못빌렸으면 한명 차감함.

    return answer

# 43mins

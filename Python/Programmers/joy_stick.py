def solution(name):
    answer = 0
    # 상하 조정횟수로 change을 채움.
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx = 0

    while True:
        answer += change[idx]  # 해당 자리 알파벳 상하조정 횟수 추가.
        change[idx] = 0  # 이미 바꾼건 0으로 초기화

        if sum(change) == 0:  # 모두 0이면 return
            return answer

        left, right = 1, 1
        while change[idx - left] == 0:  # A만날때까지 왼쪽으로 가보고
            left += 1
        while change[idx + right] == 0:  # A만날때까지 오른쪽으로 가보고
            right += 1

        answer += left if left < right else right  # 이동 횟수가 더 작은 방향으로 간다.
        idx += -left if left < right else right

    return answer

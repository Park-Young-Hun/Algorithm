def solution(prices):
    answer = []
    time = 0

    for i in range(len(prices)):  # 특정시점의 가격
        if i == len(prices) - 1:  # 마지막 주식은 무조건 0을 return
            answer.append(time)
            break

        for j in range(i + 1, len(prices)):  # 여러시점의 가격들과 비교
            if prices[j] >= prices[i]:  # 주식가격이 일정하거나 오르면 이어서 다음 시점과 비교
                time += 1
            else:  # 주식가격이 떨어졌으면 비교 중지하고 현재까지 소요시간 기록
                time += 1
                break

        answer.append(time)
        time = 0
    return answer


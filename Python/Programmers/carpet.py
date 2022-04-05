def solution(brown, yellow):
    answer = []
    sum_val = brown // 2 + 2  # 가로 + 세로
    multi_val = brown + yellow  # 가로 * 세로

    for height in range(sum_val):
        for width in range(height, sum_val):
            if width * height == multi_val and width + height == sum_val:  # 조건에 맞는지 check.
                answer.append(width)
                answer.append(height)
    return answer

# 35mins

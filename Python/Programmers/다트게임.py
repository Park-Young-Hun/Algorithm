def solution(dartResult):
    answer = 0
    value = 0
    is_ten_flag = False  # 점수가 10인 예외를 처리하기 위한 flag

    for i in range(len(dartResult)):
        if is_ten_flag:
            is_ten_flag = False
            continue

        if dartResult[i].isdigit():
            previous_value = value
            answer += value

            if dartResult[i + 1].isdigit():  # 점수가 10일 경우.
                value = int(dartResult[i] + dartResult[i + 1])
                is_ten_flag = True

            else:
                value = int(dartResult[i])
        elif dartResult[i] == 'D':
            value = value ** 2
        elif dartResult[i] == 'T':
            value = value ** 3
        elif dartResult[i] == '#':
            value *= -1
        elif dartResult[i] == '*':
            value *= 2
            answer += previous_value
    answer += value
    return answer

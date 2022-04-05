def solution(number, k):
    answer = ''
    index = 0

    while k != 0:

        if k == len(number[index:]):  # 가장 큰 수들이 중복되는 예외 체크.
            return answer

        target = number[index:index + k + 1]  # target 구간. k+1개씩 살펴본다.
        max_num = '0'

        for i in target:  # 최대값 찾기. 시간복잡도 고려해서 9찾으면 break.
            if i == '9':
                max_num = '9'
                break
            else:
                if i > max_num:
                    max_num = i

        for i in target:
            if i == max_num:  # 최대값을 찾으면 답에 추가해주고 구간 조정해주고 break.
                index += 1
                answer += i
                break
            if i < max_num:  # 최대값이 아니면 제거한다는 생각으로 k값에서 1빼주고 구간조정.
                index += 1
                k -= 1

    answer += number[index:]  # k개의 수를 제거하고 남은 뒷부분 숫자들을 추가해준다.

    return answer

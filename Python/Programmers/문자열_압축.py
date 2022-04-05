def solution(s):
    n = len(s)
    strings = []  # 분할 문자열 리스트.
    answers = []  # 완성된 압축문자열들의 길이 리스트.

    for steps in range(1, n + 1):  # 문자열을 n개씩 분할시킨 strings 리스트 생성.
        strings.append([s[i:i + steps] for i in range(0, n, steps)])

    for i in strings:
        cnt = 1
        index = 0

        while True:
            if index == len(i) - 1:  # index가 마지막일때의 예외처리.
                if cnt != 1:
                    i.insert(index, str(cnt))  # 그동안 카운팅한 같은 문자 수를 앞에 붙여줌.
                break

            if i[index] == i[index + 1]:  # 다음 index가 같은 문자라면
                cnt += 1  # 카운팅 해주고
                i.pop(index)  # 해당 문자 하나를 빼준다.
            else:  # 다음 index가 다른 문자라면
                if cnt != 1:  # 카운팅한게 있으면
                    i.insert(index, str(cnt))  # 그동안 카운팅한 같은 문자 수를 앞에 붙여줌.
                    cnt = 1

                index += 1  # 다음 index가 다른 문자라면 index를 증가 시켜줌.
        answers.append(len("".join(i)))  # 문자열로 다시 조합 후 길이를 저장.

    return min(answers)

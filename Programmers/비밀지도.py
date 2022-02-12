def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:].replace('1', '#').replace('0', ' ')

        if len(row) < n:  # 비트 연산 후,앞자리에 있어 생략된 0의 갯수만큼 공백 추가해줌.
            space = " " * (n - len(row))
            row = space + row
        answer.append(row)
    return answer

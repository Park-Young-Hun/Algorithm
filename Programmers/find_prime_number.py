from itertools import permutations


def solution(numbers):
    answer = 0
    raw_data = []

    for i in range(len(numbers)):
        obj = permutations(numbers, i + 1)  # 순열 생성.

        for j in obj:
            raw_data.append(int(''.join(j)))  # 각각의 순서쌍을 이어붙혀서 숫자로 만들어서 raw_data에 저장.

    data = list(set(raw_data))  # 중복된 숫자 제거.

    for i in data:

        flag = False

        if i == 0 or i == 1:  # 0,1은 제외
            continue

        if i == 2:  # 2는 소수로 체크하고 다음 요소로 넘어감.
            answer += 1
            continue

        for j in range(2, i):  # 소수인지 체크.

            if i % j == 0:
                flag = True
                break

        if not flag:
            answer += 1

    return answer

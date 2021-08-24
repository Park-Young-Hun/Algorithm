def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    i1 = 0
    i2 = 0
    i3 = 0

    for i in answers:

        if i1 == 5:  # index 넘어가면 0으로 초기화.
            i1 = 0

        if i2 == 8:
            i2 = 0

        if i3 == 10:
            i3 = 0

        if i == first[i1]:  # 1번 수포자가 맞혔는지 체크.
            scores[0] += 1

        if i == second[i2]:  # 2번 수포자가 맞혔는지 체크.
            scores[1] += 1

        if i == third[i3]:  # 3번 수포자가 맞혔는지 체크.
            scores[2] += 1

        i1 += 1
        i2 += 1
        i3 += 1

    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i + 1)

    return answer

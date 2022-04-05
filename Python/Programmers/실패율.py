def solution(N, stages):  # 테스트 22 실패.
    answer = []

    target = [Stage(i + 1, 0, 0, 0) for i in range(N)]

    for i in stages:
        if i <= N:
            target[i - 1].reach += 1
            target[i - 1].stay += 1

        for j in range(1, i):
            target[j - 1].reach += 1

    for i in target:
        if i.reach == 0:
            i.failure = 0
        else:
            i.failure = i.stay / i.reach

    target.sort(key=lambda x: (-x.failure, x.num))

    for i in target:
        answer.append(i.num)
    return answer


class Stage:
    def __init__(self, num, reach, stay, failure):
        self.num = num
        self.reach = reach
        self.stay = stay
        self.failure = failure


# Refactoring


def solution(N, stages):  # 통과
    answer = [[i + 1, 0] for i in range(N)]
    stay_cnt = 0

    stages.sort(reverse=True)

    for i in range(len(stages)):
        if stages[i] <= N:
            stay_cnt += 1
            answer[stages[i] - 1][1] = stay_cnt / (i + 1)

            if i < len(stages) - 1 and stages[i + 1] != stages[i]:
                stay_cnt = 0

    answer.sort(key=lambda x: -x[1])

    return [i[0] for i in answer]

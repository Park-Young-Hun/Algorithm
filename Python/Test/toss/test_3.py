from itertools import permutations


def solution(k, dungeons):
    answer = []
    dungeons_case = list(permutations(dungeons, len(dungeons)))

    for case in dungeons_case:
        life = k
        cnt = 0
        for dungeons in case:
            if dungeons[0] > life:
                break
            cnt += 1
            life -= dungeons[1]
        answer.append(cnt)

    return max(answer)

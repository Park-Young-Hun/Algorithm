from itertools import permutations


def solution(k, dungeons):
    answer = 0
    cases = list(permutations(dungeons, len(dungeons)))

    for case in cases:
        hp = k
        cnt = 0

        for need, consume in case:
            if hp < need:
                break

            hp -= consume
            cnt += 1

        if cnt > answer:
            answer = cnt

    return answer

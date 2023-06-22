import sys, math


def solution(n, l, pools):
    answer = 0
    cur = 0

    pools.sort(key=lambda x: (x[0], x[1]))

    for start, end in pools:
        if cur < start:
            cur = start

        cnt = end - cur

        if cnt > 0:
            answer += math.ceil(cnt / l)
            cur += math.ceil(cnt / l) * l

    return answer


n, l = map(int, sys.stdin.readline().split())
pools = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, l, pools))

import sys

n, k = map(int, sys.stdin.readline().split())
countries = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def solution(n, k, countries):
    country_rank = {}
    rank = 1
    cnt = 1

    countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

    for i in range(n):
        country = countries[i].pop(0)

        if i > 0:
            if countries[i] != countries[i - 1]:
                rank = cnt
        country_rank[country] = rank
        cnt += 1

    return country_rank[k]


print(solution(n, k, countries))

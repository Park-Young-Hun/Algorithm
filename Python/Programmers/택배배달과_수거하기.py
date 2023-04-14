def solution(cap, n, deliveries, pickups):
    answer = 0

    d = 0
    p = 0

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (i + 1) * 2
    return answer

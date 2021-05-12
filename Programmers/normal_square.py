import math


def solution(w, h):
    gcd = math.gcd(w, h)
    print(gcd)

    local_count = w / gcd + h / gcd - 1
    global_count = local_count * gcd

    answer = w * h - global_count
    return answer

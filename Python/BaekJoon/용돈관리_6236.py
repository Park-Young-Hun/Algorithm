import sys
from math import ceil


n, m = map(int, sys.stdin.readline().split())

moneys = [int(sys.stdin.readline()) for _ in range(n)]
sorted_moneys = sorted(moneys)


def simulate(k, money_list):
    pocket = 0
    cnt = 0
    for money in money_list:
        if cnt >= m:
            return False
        if pocket >= money:
            pocket -= money
            continue
        while money > 0:
            pocket = k
            cnt += 1
            money -= k
    if cnt > m:
        return False
    else:
        return True


def binary_search(money_list):
    left = min(money_list)
    right = max(money_list)

    while left < right:
        mid = (left + right) // 2
        print(mid)

        if simulate(mid, money_list):
            right = mid - 1
        else:
            left = mid + 1
    return mid


print(binary_search(moneys))


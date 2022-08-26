import sys


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
    left = money_list[0]
    right = money_list[-1]

    

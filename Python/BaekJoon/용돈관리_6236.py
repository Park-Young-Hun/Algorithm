import sys


n, m = map(int, sys.stdin.readline().split())

moneys = [int(sys.stdin.readline()) for _ in range(n)]
sorted_moneys = sorted(moneys)


def simulate(k, moneys) :
    pocket = 0
    cnt = 0
    for money in moneys:
        if pocket >= money:
            pocket -= money
            continue
        pocket = k
        cnt += 1



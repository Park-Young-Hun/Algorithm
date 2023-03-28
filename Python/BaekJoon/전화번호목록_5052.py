import sys
from collections import defaultdict


def solution(n, phone_nums):
    phone_dict = defaultdict(bool)

    for phone_num in phone_nums:
        phone_dict[phone_num] = True

    for phone_num in phone_nums:
        temp = ""
        for char in phone_num:
            temp += char
            if phone_dict[temp] and temp != phone_num:
                return "NO"
    return "YES"


t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    phone_nums = [sys.stdin.readline().rstrip() for _ in range(n)]

    print(solution(n, phone_nums))

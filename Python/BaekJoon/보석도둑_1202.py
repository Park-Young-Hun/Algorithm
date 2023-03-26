import sys
from bisect import bisect_left


class Gem:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


def solution(gems, bags):
    answer = 0
    is_used = [False] * (len(bags) + 1)

    for i in range(len(gems)):
        gems[i] = Gem(gems[i][0], gems[i][1])

    gems.sort(key=lambda x: (-x.value, x.weight))
    bags.sort()

    for gem in gems:
        target_index = bisect_left(bags, gem.weight)

        while is_used[target_index]:
            target_index += 1

        if target_index >= len(bags):
            continue

        is_used[target_index] = True
        answer += gem.value

    return answer


n, k = map(int, sys.stdin.readline().split())
gems = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

print(solution(gems, bags))

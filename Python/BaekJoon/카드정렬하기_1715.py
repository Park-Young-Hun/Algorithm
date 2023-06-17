import sys
import heapq


def solution(n, cards):
    answer = 0
    heapq.heapify(cards)

    while len(cards) > 1:
        a_group = heapq.heappop(cards)
        b_group = heapq.heappop(cards)

        answer += a_group + b_group
        heapq.heappush(cards, a_group + b_group)

    return answer


n = int(sys.stdin.readline())
cards = [int(sys.stdin.readline()) for _ in range(n)]
print(solution(n, cards))

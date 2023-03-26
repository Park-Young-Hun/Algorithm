import sys
import heapq


def solution(gems, bags):
    answer = 0
    values = []

    gems.sort()
    bags.sort()

    for bag in bags:
        while gems and gems[0][0] <= bag:  # 담을 수 있는 보석들 중에서
            heapq.heappush(values, -gems[0][1])  # 가격을 최대힙에 저장(음수로 저장하여 최소힙을 최대힙으로)
            heapq.heappop(gems)  # 가격 저장한 보석은 버리기

        if values:  # bag 무게 이하 보석 가격 다 저장했으면
            answer -= heapq.heappop(values)  # 제일 가치가 높은 가격 더하기(음수니까 빼기)
    return answer


n, k = map(int, sys.stdin.readline().split())
gems = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
bags = [int(sys.stdin.readline()) for _ in range(k)]

print(solution(gems, bags))

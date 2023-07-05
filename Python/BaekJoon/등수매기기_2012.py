import sys


def solution(n, expected_rank):
    answer = 0
    expected_rank.sort()

    for i in range(1, n+1):
        answer += abs(expected_rank[i-1] - i)

    return answer


n = int(sys.stdin.readline())
expected_rank = [int(sys.stdin.readline()) for _ in range(n)]
print(solution(n, expected_rank))

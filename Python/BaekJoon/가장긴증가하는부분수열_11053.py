import sys


def solution(n, A):
    dp = [1 for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
print(solution(n, arr))

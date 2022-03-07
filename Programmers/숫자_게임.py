def solution(A, B):
    answer = 0
    n = len(A)
    start = 0

    A.sort()
    B.sort()

    for i in range(n):
        for j in range(start, n):
            if B[j] > A[i]:
                answer += 1
                start = j + 1
                break
    return answer

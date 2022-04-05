import sys
from math import ceil


def solution(n, students, supervisors):
    answer = 0

    for i in students:
        if i > supervisors[0]:
            i -= supervisors[0]
            answer += 1
            if i > supervisors[1]:
                answer += ceil(i / supervisors[1])
            else:
                answer += 1
        else:
            answer += 1

    return answer


N = sys.stdin.readline()
student = list(map(int, sys.stdin.readline().split()))
supervisor = list(map(int, sys.stdin.readline().split()))
print(solution(N, student, supervisor))

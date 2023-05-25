import sys


def solution(document, target):
    answer = 0
    i = 0

    while i + len(target) <= len(document):
        if document[i:i+len(target)] == target:
            answer += 1
            i += len(target)
            continue
        i += 1

    return answer


document = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
print(solution(document, target))
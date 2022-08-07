from collections import deque

def solution(s):
    answer = []
    s = list(s)

    target = deque(s[:3])
    if len(set(target)) == 1:
            answer.append(int("".join(list(target))))

    for i in range(3, len(s)):
        target.popleft()
        target.append(s[i])
        if len(set(target)) == 1:
            answer.append(int("".join(list(target))))
    if answer:
        return max(answer)
    else:
        return -1

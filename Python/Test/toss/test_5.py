def solution(tasks):
    answer = 0
    tasks.sort()
    target = [tasks[0]]
    for i in range(1, len(tasks)):
        if target[-1] == tasks[i]:
            target.append(tasks[i])
        else:
            while target:
                n = len(target)
                if n >= 3 and (n-3)!= 1:
                    for _ in range(3):
                        target.pop()
                    answer += 1
                elif n % 2 == 0:
                    for _ in range(2):
                        target.pop()
                    answer += 1
                else:
                    return -1
            target = [tasks[i]]
    while target:
        n = len(target)
        if n >= 3 and (n-3)!= 1:
            for _ in range(3):
                target.pop()
            answer += 1
        elif n % 2 == 0:
            for _ in range(2):
                target.pop()
            answer += 1
        else:
            return -1
    return answer
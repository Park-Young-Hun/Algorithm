import sys

cases = []
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    people = []
    for j in range(n):
        people.append(list(map(int, sys.stdin.readline().split())))
    cases.append(people)

for case in cases:
    case.sort(key=lambda x: x[0])
    answer = 1
    pivot = case[0][1]
    for i in range(1, len(case)):
        if case[i][1] < pivot:
            answer += 1
            pivot = case[i][1]

    print(answer)

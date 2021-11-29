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
    answer = 0
    doc = sorted(case)
    interview = sorted(case, reverse=True)

    for i in range(1, n):
        for j in range(n):
            target = doc[i]




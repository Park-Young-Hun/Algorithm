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
    case.sort()
    case.sort(reverse=True)


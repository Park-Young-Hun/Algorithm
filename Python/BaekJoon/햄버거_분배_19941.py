import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
table = list(sys.stdin.readline())
hamburgers = []
people = deque()

for i in range(len(table)):
    if table[i] == 'H':
        hamburgers.append(i)
    else:
        people.append(i)
print(hamburgers)
print(people)

while hamburgers and people:
    person = people.popleft()

    for hamburger in hamburgers:
        if abs(hamburger-person) <= k:
            hamburgers.remove(hamburger)

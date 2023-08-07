from collections import deque
import sys

text = list(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

cursor = deque([])

for i in range(N):
    command = sys.stdin.readline().strip()

    if command[0] == "L" and text:
        a = text.pop()
        cursor.appendleft(a)
    elif command[0] == "D" and cursor:
        a = cursor.popleft()
        text.append(a)
    elif command[0] == "B" and text:
        text.pop()
    elif command[0] == "P":
        text.append(command[2])

print(''.join(text + list(cursor)))
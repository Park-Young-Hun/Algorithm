import sys


def solution():
    n = int(sys.stdin.readline())

    for _ in range(n):
        vps = sys.stdin.readline()

        stack = []
        answer = ""

        for i in vps:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack:
                    stack.pop()
                else:
                    answer = "NO"

        if answer == "":
            if stack:
                answer = "NO"
            else:
                answer = "YES"

        print(answer)


solution()

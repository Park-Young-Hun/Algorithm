import sys


def solution(target, input_string):
    stack = []

    for char in input_string:
        stack.append(char)

        if len(stack) < len(target):
            continue

        temp = stack[-len(target):]

        if "".join(temp) == target:
            for _ in range(len(target)):
                stack.pop()

    if not stack:
        stack.append("FRULA")

    return "".join(stack)


input_string = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()
print(solution(target, input_string))

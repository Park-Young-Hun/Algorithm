import sys


def solution(target, input_string):
    seperated_string = input_string.split(target)

    while len(seperated_string) > 1:
        new_string = "".join(seperated_string)
        seperated_string = new_string.split(target)

    new_string = "".join(seperated_string)

    if not new_string:
        new_string = "FRULA"
    return new_string


input_string = sys.stdin.readline().rstrip()
target = sys.stdin.readline().rstrip()

print(solution(target, input_string))

import sys


def solution(n, numbers, operators):
    value = numbers[0]

    numbers.sort()
    for i in range(1, n):
        if operators[1] != 0:
            value -= numbers[i]
            operators[1] -= 1
        elif operators[3] != 0:
            if value < 0 and numbers[1] < 0:
                value = -value // -numbers[i]
            elif value < 0:
                value = -(-value // numbers[i])
            else:
                value //= numbers[i]
            operators[3] -= 1
        elif operators[0] != 0:
            value += numbers[i]
            operators[0] -= 1
        else:
            value *= numbers[i]
            operators[2] -= 1
    return value


N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split()))
print(solution(N, num, operator))

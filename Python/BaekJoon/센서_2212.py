import sys


def solution(n, k, sensors):
    sections = []

    sensors = list(set(sensors))
    sensors.sort()

    if k >= len(sensors):
        return 0

    for i in range(len(sensors) - 1):
        sections.append(sensors[i + 1] - sensors[i])

    sections.sort()

    for _ in range(k - 1):
        sections.pop()

    return sum(sections)


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
sensors = list(map(int, sys.stdin.readline().split()))

print(solution(n, k, sensors))

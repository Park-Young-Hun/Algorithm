import sys

n, c = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(n)]
houses.sort()


def solution(n, c, houses):
    answer = []
    left = 0
    right = n-1
    c -= 2

    while c > 0 and left <= right:
        mid = (left + right) // 2
        left_distance = houses[mid] - houses[left]
        right_distance = houses[right] - houses[mid]

        if left_distance > right_distance:
            right = mid
            answer.append(right_distance)
        else:
            left = mid
            answer.append(left_distance)
        c -= 1
    #print(answer)
    return max(answer)


print(solution(n, c, houses))

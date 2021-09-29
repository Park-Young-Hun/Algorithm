def solution(n, times):
    answer = 0

    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2

        count = 0

        for time in times:
            count += mid // time

        if count >= n:
            right = mid - 1
        else:
            left = mid + 1

    answer = left
    return answer

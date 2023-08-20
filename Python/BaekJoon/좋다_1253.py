import sys


def solution(n, nums):
    answer = 0
    nums.sort()

    for i in range(n):
        temp = nums[:i] + nums[i+1:]

        left = 0
        right = len(temp) - 1

        while left < right:
            sum_val = temp[left] + temp[right]

            if sum_val == nums[i]:
                answer += 1
                break
            elif sum_val > nums[i]:
                right -= 1
            else:
                left += 1

    return answer


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(solution(n, nums))

import sys
from collections import defaultdict
from copy import deepcopy


def solution(n, nums):
    answer = 0
    nums.sort()

    nums_cnt = defaultdict(int)

    for num in nums:
        nums_cnt[num] += 1

    for target in nums:
        temp_cnt = deepcopy(nums_cnt)

        for num in nums:
            if temp_cnt[num] > 0:
                temp_cnt[num] -= 1

                if temp_cnt[target - num] > 0 and target != target - num:
                    temp_cnt[target - num] -= 1
                    answer += 1
                    break
                else:
                    temp_cnt[num] += 1

    return answer


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(solution(n, nums))

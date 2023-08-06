import sys


def solution(n, nums):
    answer = set()

    for i in range(n):
        visited = [False] * (n+1)
        temp = [i+1]
        visited[i+1] = True

        child = nums[i]

        while not visited[child]:
            temp.append(child)
            visited[child] = True

            child = nums[child-1]

        temp.append(child)

        if temp[0] == temp[-1]:
            for j in range(len(temp)-1):
                answer.add(temp[j])

    return sorted(list(answer))


n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
answer = solution(n, nums)
print(len(answer))

for num in answer:
    print(num)

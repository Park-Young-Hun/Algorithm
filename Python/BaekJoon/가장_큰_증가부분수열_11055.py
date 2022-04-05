import sys


def solution(n, num_list):
    dp = [num_list[0]]  # 각 자릿수까지의 최대 부분수열의 합

    for i in range(1, n):
        temp = []
        for j in range(i):  # 지금까지 만들어진 dp 리스트를 순회하면서
            if num_list[j] < num_list[i]:  # 만약 num_list의 값이 현재 값보다 작다면
                temp.append(dp[j])  # 그 인덱스에 해당하는 dp 리스트 값을 저장.

        if temp:
            dp.append(max(temp) + num_list[i])  # 현재 값보다 작은 값들 중 가장 큰 dp값을 더함.
        else:
            dp.append(num_list[i])  # 현재 값이 제일 작으면 해당 값만 dp 리스트에 추가.

    return max(dp)


N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
print(solution(N, nums))



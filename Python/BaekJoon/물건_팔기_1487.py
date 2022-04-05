import sys

n = int(sys.stdin.readline())

cost = []

for _ in range(n):  # [가격, 배달비] 형태로 생성.
    temp = list(map(int, sys.stdin.readline().split()))
    cost.append([temp[0], temp[1]])

cost.sort(key=lambda x: (x[0], x[1]))  # 가격, 배달비 순으로 정렬.

total = [0] * n  # 가격이 n일 때의 총이익.

for i in range(n):
    for j in range(i, n):  # 기준 가격 n
        benefit = cost[i][0] - cost[j][1]  # 가격은 기준 가격이지만 배달비는 원래 정해진대로.
        if benefit > 0:  # 이득일 경우에만 판다.
            total[i] += benefit

result = [cost[i][0] for i in range(n) if total[i] == max(total)]  # 최대 이익을 내는 기준 가격들 다모은다.

if sum(total) == 0:  # 이익을 내는 경우가 없다.
    print(0)
else:
    print(min(result))  # 최대 이익을 내는 기준 가격 중 제일 낮은거 출력.


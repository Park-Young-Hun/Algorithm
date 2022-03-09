import sys
from itertools import combinations


cases = []
result = []

n = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nums = [i+1 for i in range(n)]
comb = list(combinations(nums, n//2))  # 한개의 팀 인원만큼 선택하는 경우의 수.

for i in range(len(comb)//2):  # 각각 한개의 팀원만큼 선택한 경우의 수에 대하여 짝이 맞도록 2개씩 묶어줌.
    cases.append([comb[i], comb[len(comb)-(i+1)]])

for case in cases:
    target_1 = list(combinations(case[0], 2))  # 한팀에 대하여 점수 계산을 위해 두 선수씩 묶어줌.
    target_2 = list(combinations(case[1], 2))

    team_1_score = sum([table[i[0]-1][i[1]-1] + table[i[1]-1][i[0]-1] for i in target_1])  # 점수 계산
    team_2_score = sum([table[i[0]-1][i[1]-1] + table[i[1]-1][i[0]-1] for i in target_2])

    result.append(abs(team_1_score - team_2_score))

print(min(result))

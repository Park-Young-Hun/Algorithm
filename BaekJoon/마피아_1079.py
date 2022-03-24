import sys
from copy import deepcopy


answer = []
n = int(sys.stdin.readline())
guilty = list(map(int, sys.stdin.readline().split()))
R = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
mafia = int(sys.stdin.readline())

cnt = 0
mafia_target = []



for i in range(n):
    if i != mafia:
        mafia_target.append((i, R[i][mafia]))

citizen_target = [[i, guilty[i]] for i in range(n)]

for index in range(n):
    temp_mafia_target = deepcopy(mafia_target)
    survivor = [i for i in range(n)]

    while len(survivor) != 1:

        if len(survivor) % 2 == 0:  # 밤이 찾아왔습니다.
            victim = temp_mafia_target.pop(index)
            survivor.remove(victim[0])
            cnt += 1

            for i in citizen_target:
                if i[0] == victim[0]:
                    citizen_target.remove(i)
                    break

            for i in citizen_target:
                if i[0] == mafia:
                    i[1] += victim[1]
                    guilty[i[0]] += victim[1]
                else:
                    i[1] += R[victim[0]][i[0]]
                    guilty[i[0]] += R[victim[0]][i[0]]

            if len(survivor) == 1:
                break

        else:  # 낮이 밝았습니다.
            citizen_target.sort(key=lambda x: (x[1], -x[0]))
            victim = citizen_target.pop()
            survivor.remove(victim[0])

            if victim[0] == mafia:
                break

            for i in temp_mafia_target:
                if i[0] == victim[0]:
                    temp_mafia_target.remove(i)
                    break

    answer.append(cnt)
print(answer)
print(max(answer))



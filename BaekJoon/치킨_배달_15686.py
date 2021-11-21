import sys
from itertools import combinations


def calculate(stores):
    result = 0
    for k in home:
        result += min([abs(l[0] - k[0]) + abs(l[1] - k[1]) for l in stores])

    return result


n, m = map(int, sys.stdin.readline().split())

answer = []
table = []
store = []
home = []

for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if table[i][j] == 2:
            store.append([i, j])
        elif table[i][j] == 1:
            home.append([i, j])

close = len(store) - m
targets = list(combinations(store, close))

for target in targets:
    temp = store[:]  # 재할당할땐 복사본으로. (그렇지 않으면 temp과 store가 같은 메모리 주소를 공유하기 때문에 둘다 바뀜)
    for i in target:
        temp.remove(i)
    answer.append(calculate(temp))

print(min(answer))

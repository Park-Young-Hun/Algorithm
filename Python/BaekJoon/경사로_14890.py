import sys

N, L = map(int, sys.stdin.readline().split())
rows = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cols = []

for i in range(N):
    col = []
    for j in range(N):
        col.append(rows[j][i])
    cols.append(col)

roads = rows + cols


def can_pass(N, L, road):
    length = 1  # 같은 높이의 칸 갯수
    i = 1

    while i < N:
        if road[i] == road[i-1]:
            length += 1
            i += 1
            if length > L:  # 최대 L까지만 count
                length = L
            continue

        gap = road[i] - road[i-1]

        if abs(gap) > 1:
            return False

        if gap == 1:  # 오르막
            if length != L:  # 경사로 만들 칸부족.
                return False
            length = 1  # 오르막 끝 지점의 높은 칸은 바로 경사로를 만드는데 활용 가능 -> 1로 초기화.
        elif gap == -1:  # 내리막
            if L <= N-i:  # 경사로를 만들 칸이 충분하다면
                for j in range(i, i + L):  # L개의 칸이 모두 같은 높인지 확인.
                    if road[j] != road[i]:
                        return False
                i = j  # index 확인한 만큼 반영.
                length = 0  # 내리막 끝 지점의 낮은 칸은 경사로에 이미 활용되었기 때문에 -> 0으로 초기화.
            else:
                return False
        i += 1
    return True


def solution(N, L, roads):
    answer = 0

    for road in roads:
        if can_pass(N, L, road):
            answer += 1

    return answer


print(solution(N, L, roads))

import sys


def solution(h, w, blocks):
    result = 0

    for i in range(1, w - 1):  # 맨 왼쪽과 맨 오른쪽은 고일 수 없다.
        left_max = max(blocks[:i])  # 왼쪽에서 제일 높은 블록
        right_max = max(blocks[i + 1:])  # 오른쪽에서 제일 높은 블록

        lower_one = min(left_max, right_max)  # 그중 가장 낮은 블록

        if blocks[i] < lower_one:  # 현재 블록이 lower_one 블록 보다는 낮아야 빗물이 고인다.
            result += lower_one - blocks[i]
    return result


h, w = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))
print(solution(h, w, blocks))

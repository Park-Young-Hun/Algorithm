import sys
from collections import deque


def solution(n, m, h, storage):
    day = 0
    unripe_cnt = 0
    q = deque()
    delta = [
        (1, 0, 0), (-1, 0, 0), (0, 1, 0),
        (0, -1, 0), (0, 0, 1), (0, 0, -1)
    ]

    for i in range(h):
        for j in range(m):
            for k in range(n):
                if storage[i][j][k] == 1:
                    q.append((i, j, k))
                elif storage[i][j][k] == 0:
                    unripe_cnt += 1

    if unripe_cnt == 0:
        return day

    while q:
        for _ in range(len(q)):
            height, row, col = q.popleft()

            for delta_h, delta_row, delta_col in delta:
                new_height = height + delta_h
                new_row = row + delta_row
                new_col = col + delta_col

                if new_height < 0 or new_height >= h or new_row < 0 or new_row >= m or new_col < 0 or new_col >= n:
                    continue
                if storage[new_height][new_row][new_col] == 0:
                    q.append((new_height, new_row, new_col))
                    storage[new_height][new_row][new_col] = 1
                    unripe_cnt -= 1
        if q:
            day += 1

    if unripe_cnt > 0:
        return -1

    return day


n, m, h = map(int, sys.stdin.readline().split())
storage = []

for _ in range(h):
    storage.append([list(map(int, sys.stdin.readline().split())) for _ in range(m)])

print(solution(n, m, h, storage))




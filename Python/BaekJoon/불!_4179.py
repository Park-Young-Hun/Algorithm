import sys
from collections import deque


def solution(miro):
    time = 0
    delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    j_visited = [[False] * c for _ in range(r)]
    j_q = deque()
    fire_q = deque()

    for i in range(r):
        for j in range(c):
            if miro[i][j] == 'J':
                miro[i][j] = '.'
                j_q.append((i, j))
            elif miro[i][j] == 'F':
                fire_q.append((i, j))

    while j_q:  # 지훈이가 갈 곳이 있다면
        for _ in range(len(fire_q)):  # 먼저 불 확산.
            row, col = fire_q.popleft()

            for i in range(4):
                delta_row, delta_col = delta[i]
                new_row = row + delta_row
                new_col = col + delta_col

                if new_row < 0 or new_row >= r or new_col < 0 or new_col >= c:
                    continue

                if miro[new_row][new_col] == '.':
                    miro[new_row][new_col] = 'F'
                    fire_q.append((new_row, new_col))

        for _ in range(len(j_q)):  # BFS로 지훈이가 다음 타임에 갈 방향 탐색.
            row, col = j_q.popleft()

            for i in range(4):
                delta_row, delta_col = delta[i]
                new_row = row + delta_row
                new_col = col + delta_col

                if new_row < 0 or new_row >= r or new_col < 0 or new_col >= c:  # 경계 지점에 있으면 다음 타임에 탈출 확정.
                    return time + 1

                if not j_visited[new_row][new_col] and miro[new_row][new_col] == '.':
                    j_visited[new_row][new_col] = True
                    j_q.append((new_row, new_col))
        time += 1

    # 갈 곳이 더이상 없다면
    return "IMPOSSIBLE"


r, c = map(int, sys.stdin.readline().split())
miro = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

print(solution(miro))

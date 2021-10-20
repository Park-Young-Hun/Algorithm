from collections import deque


def solution(rows, columns, queries):
    answer = []
    matrix = []

    for i in range(rows):  # 행렬 만들기.
        matrix.append([i * columns + (j + 1) for j in range(columns)])

    for query in queries:
        border = []  # 테두리 숫자들 저장.
        buffer = deque()
        buffer.append(matrix[query[0] - 1][query[1] - 1])

        for i in range(query[1], query[3]):
            border.append(matrix[query[0] - 1][i])
            buffer.append(matrix[query[0] - 1][i])
            matrix[query[0] - 1][i] = buffer.popleft()

        for j in range(query[0], query[2]):
            border.append(matrix[j][query[3] - 1])
            buffer.append(matrix[j][query[3] - 1])
            matrix[j][query[3] - 1] = buffer.popleft()

        for k in range(query[3], query[1], -1):
            border.append(matrix[query[2] - 1][k - 2])
            buffer.append(matrix[query[2] - 1][k - 2])
            matrix[query[2] - 1][k - 2] = buffer.popleft()

        for l in range(query[2], query[0], -1):
            border.append(matrix[l - 2][query[1] - 1])
            buffer.append(matrix[l - 2][query[1] - 1])
            matrix[l - 2][query[1] - 1] = buffer.popleft()

        answer.append(min(border))

    return answer

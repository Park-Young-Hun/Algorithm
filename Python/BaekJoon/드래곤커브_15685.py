import sys


def solution(N, curves):
    answer = 0
    direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    is_in_curve = [[False] * 101 for _ in range(101)]

    for curve in curves:
        col, row, way, gen = curve
        points = [(row, col)]
        delta_row, delta_col = direction[way]

        points.append((row + delta_row, col + delta_col))

        while gen > 0:
            axis = points[-1]  # 끝점이 회전축

            for i in range(len(points)-2, -1, -1):  # 끝점을 제외하고 모든 점들을 270도 회전변환 수행.
                row, col = points[i]
                row -= axis[0]  # 원점으로 이동
                col -= axis[1]

                temp = row  # 원점기준 270도 회전변환 수행.
                row = col  # X' = cos 270º X - sin 270º Y = Y
                col = -temp  # Y' = sin 270º X + cos 270º Y = - X

                row += axis[0]  # 다시 원래 위치로 이동.
                col += axis[1]
                points.append((row, col))
            gen -= 1

        for point in points:
            row, col = point
            is_in_curve[row][col] = True

    for i in range(100):
        for j in range(100):
            square = [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]
            is_square = True

            for row, col in square:
                if not is_in_curve[row][col]:
                    is_square = False
                    break

            if is_square:
                answer += 1

    return answer


N = int(sys.stdin.readline())
curves = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(solution(N, curves))

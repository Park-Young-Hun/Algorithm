def solution(m, n, puddles):
    answer = 0
    road_map = []

    for i in range(n):
        road_map.append([-1 for j in range(m)])  # -1로 다 채워주기.

    road_map[0][0] = 1  # 출발점

    for i in puddles:  # 물에 잠긴 지역은 0으로.
        road_map[i[1] - 1][i[0] - 1] = 0

    for i in range(n):
        for j in range(m):
            if road_map[i][j] == -1:  # 위쪽 boundary
                if i == 0:
                    road_map[i][j] = road_map[i][j - 1]
                elif j == 0:  # 왼쪽 boundary
                    road_map[i][j] = road_map[i - 1][j]
                else:  # 일반적인 경우
                    road_map[i][j] = road_map[i - 1][j] + road_map[i][j - 1]

    answer = road_map[n - 1][m - 1] % 1000000007

    return answer

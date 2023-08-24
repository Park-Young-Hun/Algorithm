def solution(want, number, discount):
    answer = 0
    wanted_items = []
    MAX_WINDOW_LEN = 10

    for i in range(len(want)):
        for _ in range(number[i]):
            wanted_items.append(want[i])

    wanted_items.sort()

    for i in range(len(discount) - MAX_WINDOW_LEN + 1):
        window = discount[i:i + MAX_WINDOW_LEN]
        window.sort()

        if window == wanted_items:
            answer += 1

    return answer

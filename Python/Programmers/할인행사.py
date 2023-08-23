from collections import deque, defaultdict


def solution(want, number, discount):
    answer = 0
    MAX_WINDOW_LEN = 10
    window = deque()
    discount = deque(discount)
    want_cnts = defaultdict(int)

    for i in range(len(want)):
        want_cnts[want[i]] = number[i]

    for _ in range(MAX_WINDOW_LEN):
        item = discount.popleft()
        window.append(item)

        if want_cnts[item] > 0:
            want_cnts[item] -= 1

    if sum(want_cnts.values()) == 0:
        answer += 1

    while discount:
        item = window.popleft()

        if want_cnts[item] > 0:
            want_cnts[item] += 1

        new_item = discount.popleft()
        window.append(new_item)

        if want_cnts[new_item] > 0:
            want_cnts[new_item] -= 1

        if sum(want_cnts.values()) == 0:
            answer += 1

    return answer

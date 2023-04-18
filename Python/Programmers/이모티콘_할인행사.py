from itertools import product


def solution(users, emoticons):
    answer = []
    m = len(emoticons)
    discount = [10, 20, 30, 40]

    cases = list(product(discount, repeat=m))

    for case in cases:
        sub = 0
        amount = 0

        prices = []
        for i in range(m):
            prices.append((emoticons[i] // 100) * (100 - case[i]))

        for target, threshold in users:
            money = 0

            for i in range(m):
                if case[i] >= target:
                    money += prices[i]
            if money >= threshold:
                sub += 1
            else:
                amount += money
        answer.append((sub, amount))

    answer.sort(key=lambda x: (-x[0], -x[1]))

    return answer[0]

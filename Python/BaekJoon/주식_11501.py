import sys


def solution(n, stock_prices):
    day_prices = list(enumerate(stock_prices))
    day_prices.sort(key=lambda x: (-x[1], -x[0]))
    result = 0
    today = 0

    for day, price in day_prices:
        if day > today:
            for i in range(today, day):
                profit = price - stock_prices[i]

                if profit > 0:
                    result += profit
            today = day + 1
    return result


t = int(sys.stdin.readline())
answers = []

for _ in range(t):
    n = int(sys.stdin.readline())
    stock_prices = list(map(int, sys.stdin.readline().split()))
    answers.append(solution(n, stock_prices))

for answer in answers:
    print(answer)


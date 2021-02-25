N = int(input())

five_kg = N // 5  # 5킬로 봉지 수
five_remainder = N % 5  # 5킬로 봉지에 담고 남은 설탕
three_kg = five_remainder // 3  # 3킬로 봉지 수
three_remainder = five_remainder % 3  # 3킬로 봉지에 담고 남은 설탕(0이 되어야 정상 case)

if three_remainder == 0:
    print(five_kg + three_kg)
else:  # 이미 담은 5킬로 봉지를 하나씩 풀어서 3키로 봉지로 나누어 떨어지는지 확인.
    while True:
        if five_kg == 0:
            print(-1)
            break
        five_kg -= 1
        three_remainder += 5
        three_kg += three_remainder // 3
        three_remainder %= 3

        if three_remainder == 0:
            print(five_kg + three_kg)
            break

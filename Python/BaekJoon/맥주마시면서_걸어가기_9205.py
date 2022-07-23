import sys
import math

home = []
store = []
festival = []
store_nums = []

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    store_nums.append(n)
    home.append(tuple(map(int, sys.stdin.readline().split())))

    if n > 0:
        temp_store = []
        for j in range(n):
            temp_store.append(tuple(map(int, sys.stdin.readline().split())))

        store.append(temp_store)

    festival.append(tuple(map(int, sys.stdin.readline().split())))

for i in range(t):
    beers = 20
    answer = ""
    n = store_nums[i]

    if n == 0:
        distance = abs(festival[i][0] - home[i][0]) + abs(festival[i][1] - home[i][1])
        needs = math.ceil(distance / 50)
        if needs > beers:
            answer = "sad"
        else:
            answer = "happy"
        print(answer)
        continue

    distance = abs(store[i][0][0] - home[i][0]) + abs(store[i][0][1] - home[i][1])
    needs = math.ceil(distance / 50)
    if needs > beers:
        answer = "sad"
        print(answer)
        continue

    if n > 1:
        for j in range(1, n):
            beers = 20
            distance = abs(store[i][j][0] - store[i][j - 1][0]) + abs(store[i][j][1] - store[i][j - 1][1])
            needs = math.ceil(distance / 50)
            if needs > beers:
                answer = "sad"
                break
        if answer == "sad":
            print(answer)
            continue
    distance = abs(festival[i][0] - store[i][n-1][0]) + abs(festival[i][1] - store[i][n-1][1])
    needs = math.ceil(distance / 50)

    if needs > beers:
        answer = "sad"
    else:
        answer = "happy"
    print(answer)

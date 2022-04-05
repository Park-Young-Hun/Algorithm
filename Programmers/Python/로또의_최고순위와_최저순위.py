def solution(lottos, win_nums):
    answer = []
    rank = [6, 5, 4, 3, 2, 1]
    match = 0
    unknown = 0

    for lotto in lottos:
        if lotto == 0:
            unknown += 1
            continue
        for win_num in win_nums:
            if lotto == win_num:
                match += 1
                break
    if match == 0:
        if unknown == 0:
            answer.append(6)
        else:
            answer.append(rank.index(unknown) + 1)

        answer.append(6)

    else:
        answer.append(rank.index(match + unknown) + 1)
        answer.append(rank.index(match) + 1)

    return answer

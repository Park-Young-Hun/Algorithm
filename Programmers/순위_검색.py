from collections import defaultdict
from itertools import product
from bisect import bisect_left


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in range(len(info)):
        info[i] = info[i].split()
        info[i][-1] = int(info[i][-1])
    info.sort(key=lambda x: x[4])

    for i in info:
        key_set = product([i[0], '-'], [i[1], '-'], [i[2], '-'], [i[3], '-'], )

        for j in key_set:
            info_dict["".join(j[:4])].append(i[-1])

    for i in range(len(query)):
        query[i] = query[i].replace("and", "")
        query[i] = query[i].split()
        query[i] = ["".join(query[i][:4]), int(query[i][-1])]

    for i in query:
        answer.append(len(info_dict[i[0]]) - bisect_left(info_dict[i[0]], i[1]))

    return answer

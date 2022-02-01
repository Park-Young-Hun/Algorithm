from collections import defaultdict


def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in range(len(info)):
        info[i] = info[i].split()
        info[i][-1] = int(info[i][-1])
    info.sort(key=lambda x: x[4])

    for i in info:
        info_dict["".join(i[:4])].append(i[-1])

    for i in range(len(query)):
        query[i] = query[i].replace("and", "")
        query[i] = query[i].split()
        query[i] = ["".join(query[i][:4]), query[i][-1]]
    print(query)
    info_keys = info_dict.keys()
    print(info_dict)

    return answer

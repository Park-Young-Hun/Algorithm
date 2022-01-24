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
        # query[i] = list(filter(lambda a: a != 'and', query[i]))
        # query[i][-1] = int(query[i][-1])

    print(query)
    info_keys = info_dict.keys()
    print(info_dict)

    #     for i in query:
    #         cnt = 0
    #         differ_flag = False
    #         #print(info_keys)

    #         for j in info_keys:
    #             if i[-1] > j:
    #                 #print("pass", i[-1])
    #                 break
    #             for k in info_dict[j]:
    #                 #print("i", k, m)
    #                 for n in range(4):
    #                     if i[n] != '-' and i[n] != k[n]:
    #                         differ_flag = True
    #                         break
    #                 if not differ_flag:
    #                     cnt += 1
    #                 else:
    #                     differ_flag = False

    #         answer.append(cnt)
    #         #print(cnt)
    #         cnt = 0

    return answer

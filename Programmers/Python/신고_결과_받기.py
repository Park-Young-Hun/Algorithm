from collections import defaultdict


def solution(id_list, report, k):
    report_id_dict = defaultdict(list)
    report_dict = defaultdict(int)
    email_dict = defaultdict(int)

    for i in id_list:
        email_dict[i] = 0

    for i in report:
        ids = i.split()
        if ids[1] not in report_id_dict[ids[0]]:
            report_id_dict[ids[0]].append(ids[1])
            report_dict[ids[1]] += 1

    for i in report_id_dict.keys():
        for j in report_id_dict[i]:
            if report_dict[j] >= k:
                email_dict[i] += 1

    return list(email_dict.values())

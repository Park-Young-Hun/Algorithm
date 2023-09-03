from collections import defaultdict, deque


def solution(input_string):
    answer = set()

    chr_cnts = defaultdict(int)
    appear_dict = defaultdict(bool)
    window = deque()

    for i in range(len(input_string)):
        chr_cnts[input_string[i]] += 1

        if window:
            if window[-1] == input_string[i]:
                window.append(input_string[i])
            if window[-1] != input_string[i] or i == len(input_string) - 1:
                target = window[-1]

                if appear_dict[target] and chr_cnts[target] >= 2:
                    answer.add(target)

                appear_dict[target] = True
                window.clear()
                window.append(input_string[i])

                if i == len(input_string) - 1 and target != input_string[i]:
                    if appear_dict[input_string[i]] and chr_cnts[input_string[i]] >= 2:
                        answer.add(input_string[i])
        else:
            window.append(input_string[i])

    answer = list(answer)

    if answer:
        answer.sort()
        answer = "".join(answer)
    else:
        answer = "N"

    return answer

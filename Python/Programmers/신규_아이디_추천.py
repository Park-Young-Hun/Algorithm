def solution(new_id):
    target = "0123456789abcdefghijklmnopqrstuvwxyz-_."
    new_id = list(new_id)
    i = 0
    j = 0
    dot_cnt = 0

    while i < len(new_id):  # 1, 2단계
        new_id[i] = new_id[i].lower()

        if new_id[i] not in target:
            new_id.remove(new_id[i])
            i -= 1
        i += 1

    while j < len(new_id):  # 3단계

        if new_id[j] == '.':
            dot_cnt += 1
            if dot_cnt > 1:
                new_id.pop(j)
            else:
                j += 1
        else:
            dot_cnt = 0
            j += 1

    if len(new_id) != 0 and new_id[0] == '.':  # 4단계
        new_id.pop(0)
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id.pop(-1)

    if not new_id:  # 5단계
        new_id.append('a')

    if len(new_id) >= 16:  # 6단계
        new_id = new_id[:15]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id.pop(-1)

    if len(new_id) <= 2:  # 7단계
        while len(new_id) < 3:
            new_id.append(new_id[-1])

    return "".join(new_id)

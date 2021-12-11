def solution(new_id):
    answer = ''
    target = "0123456789abcdefghijklmnopqrstuvwxyz-_."
    new_id = list(new_id)
    i = 0
    j = 0
    dot_cnt = 0

    while i < len(new_id):
        new_id[i] = new_id[i].lower()

        if new_id[i] not in target:
            new_id.remove(new_id[i])
            i -= 1
        i += 1

    while j < len(new_id):
        print(dot_cnt)
        if new_id[j] == '.':
            dot_cnt += 1
            if dot_cnt > 1:
                new_id.remove(new_id[j])
            else:
                j += 1
        else:
            dot_cnt = 0
            j += 1
    print(new_id)
    return answer


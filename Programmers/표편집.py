def solution(n, k, cmd):
    table = {x: [x - 1, x + 1] for x in range(n)}
    answer = ['O' for _ in range(n)]
    clear = []

    for c in cmd:
        detail = c.split()

        if detail[0] == 'C':
            before, after = table[k]
            clear.append((before, after, k))
            answer[k] = 'X'

            if before == -1:
                table[after][0] = before
                k = after
            elif after == n:
                table[before][1] = after
                k = before
            else:
                table[before][1] = after
                table[after][0] = before
                k = after
        elif c == 'Z':
            before, after, num = clear.pop()
            answer[num] = 'O'

            if before == -1:
                table[after][0] = num
            elif after == n:
                table[before][1] = num
            else:
                table[before][1] = num
                table[after][0] = num

        elif detail[0] == 'U':
            for _ in range(int(detail[1])):
                k = table[k][0]
        elif detail[0] == 'D':
            for _ in range(int(detail[1])):
                k = table[k][1]

    return ''.join(answer)

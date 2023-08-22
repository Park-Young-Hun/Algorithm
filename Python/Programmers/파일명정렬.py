def solution(files):
    answer = []

    for i in range(len(files)):
        head = ""

        for j in range(len(files[i])):
            if files[i][j].isdigit() and not head:
                head = files[i][:j]
                head_end = j

            if head:
                if not files[i][j].isdigit():
                    num = files[i][head_end:j]
                    tail = files[i][j:]
                    break

            if j == len(files[i]) - 1:
                num = files[i][head_end:j + 1]
                tail = ""

        answer.append([head, num, tail, i])

    answer.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))

    for i in range(len(answer)):
        answer[i] = "".join(answer[i][:3])

    return answer

def solution(w, h):
    input_w = w
    input_h = h
    i = 2

    while i < 10:
        if (w % i == 0) and (h % i == 0):
            w /= i
            h /= i
        else:
            i += 1

    interval = w + h - 1
    count = interval
    temp_w = w
    temp_h = h

    while 1:
        if w < input_w:
            w += temp_w
            h += temp_h
            count += interval
        else:
            break

    answer = input_w * input_h - count
    return answer

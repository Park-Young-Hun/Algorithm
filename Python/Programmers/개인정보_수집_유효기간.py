def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    now_year, now_month, now_day = map(int, today.split('.'))
    now_date = now_year * 12 * 28 + now_month * 28 + now_day

    for term in terms:
        kind, month = term.split()
        term_dict[kind] = int(month)

    for i in range(len(privacies)):
        date, kind = privacies[i].split()

        year, month, day = map(int, date.split('.'))
        month += term_dict[kind]
        date = year * 12 * 28 + month * 28 + day

        if now_date >= date:
            answer.append(i + 1)
    return answer

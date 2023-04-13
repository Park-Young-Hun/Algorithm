def calc_date(kind, year, month, day):
    month += term_dict[kind]

    if month > 12:
        share, remainder = divmod(month, 12)

        if remainder == 0:
            share -= 1
            remainder = 12
        year += share
        month = remainder

    return year, month, day


def solution(today, terms, privacies):
    answer = []
    global term_dict
    term_dict = {}

    for term in terms:
        kind, month = term.split()
        term_dict[kind] = int(month)

    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        year, month, day = map(int, date.split('.'))

        year, month, day = calc_date(kind, year, month, day)
        now_year, now_month, now_day = map(int, today.split('.'))

        if now_year > year:
            answer.append(i + 1)

        if now_year == year:
            if now_month > month:
                answer.append(i + 1)
            if now_month == month and now_day >= day:
                answer.append(i + 1)
    return answer

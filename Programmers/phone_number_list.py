def solution(phone_book):
    answer = True
    phone_book.sort()  # 문자열들을 문자순으로 정렬. 앞에서 부터 같은 문자열을 포함하는 것들은 서로 인접할 수 밖에 없다.

    for i in range(len(phone_book)):

        if i != len(phone_book) - 1:
            target = phone_book[i + 1][:len(phone_book[i])]  # target은 다음 문자열을 현재 문자열 크기로 자른 것.

            if target == phone_book[i]:  # 인접한 두 문자열을 같은 크기로 비교.
                answer = False
                return answer

    return answer

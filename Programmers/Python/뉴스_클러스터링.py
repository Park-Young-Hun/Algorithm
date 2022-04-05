def solution(str1, str2):
    strs = [list(str1.lower()), list(str2.lower())]

    for i in strs:  # 두 글자씩 끊어서 다중집합 만들기.
        for j in range(len(i) - 1):
            i[j] += i[j + 1]
        i.pop()

    for i in strs:  # 영문이 아닌 문자를 포함한 글자 쌍은 제외.
        for j in i[:]:
            for k in j:
                if ord(k) < 97 or ord(k) > 122:
                    i.remove(j)
                    break
    strs.sort(key=len)  # 길이가 작은 리스트를 바깥 루프로 돌릴 예정(시간 복잡도 고려).

    return int(jaccard(strs) * 65536)


def jaccard(str_arr):  # 자카드 유사도 측정.
    if str_arr[0] or str_arr[1]:
        u = str_arr[0] + str_arr[1]  # 전체 집합.
        intersection = []

        for i in str_arr[0]:
            for j in str_arr[1]:
                if i == j:  # 공통된 부분으로 교집합을 만들어줌.
                    intersection.append(i)
                    str_arr[1].remove(j)
                    break

        return len(intersection) / (len(u) - len(intersection))  # 교집합을 구하면 합집합은 원소 갯수로 파악가능.
    else:  # 둘 다 공집합일 경우.
        return 1

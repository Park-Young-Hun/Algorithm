import sys


def solution(word):
    cnt = [0] * 26
    word = word.lower()

    for letter in word:
        if letter != '\n':
            cnt[ord(letter) - 97] += 1

    sorted_cnt = sorted(cnt, reverse=True)

    if sorted_cnt[0] == sorted_cnt[1]:
        return '?'
    else:
        return chr(cnt.index(sorted_cnt[0]) + 97).upper()


if __name__ == "__main__":
    input_word = sys.stdin.readline()
    print(solution(input_word))

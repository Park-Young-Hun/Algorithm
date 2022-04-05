def solution(s):
    nums = [str(i) for i in range(10)]
    en_nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    word = []
    s = list(s)
    i = 0

    while True:

        if "".join(word) in en_nums:
            s.insert(i, str(en_nums.index("".join(word))))
            word = []
            i += 1
        elif s[i] not in nums:
            word.append(s[i])
            s.remove(s[i])
        else:
            i += 1

        if i >= len(s):
            if word:
                s.insert(i, str(en_nums.index("".join(word))))
                break
            else:
                break

    return int("".join(s))

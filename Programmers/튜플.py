def solution(s):
    answer = []

    s_list = []
    nums = []
    temp_nums = ""

    for i in s:
        if i.isdigit():
            temp_nums += i
        elif i == ',':
            if temp_nums:
                nums.append(int(temp_nums))
            temp_nums = ""
        elif i == '}':
            if temp_nums:
                nums.append(int(temp_nums))
                s_list.append(nums)
            temp_nums = ""
            nums = []

    s_list.sort(key=lambda x: len(x))

    for i in s_list:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer

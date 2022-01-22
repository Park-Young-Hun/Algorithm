def solution(s):
    max_len_tuples = []
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
            temp_nums = ""

            if len(nums) > len(max_len_tuples):
                max_len_tuples = nums
            print(max_len_tuples)
            nums = []

    return max_len_tuples

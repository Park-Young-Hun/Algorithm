def solution(array, commands):
    answer = []
    arr = []

    for i in commands:
        arr = sorted(array[i[0] - 1:i[1]])
        answer.append(arr[i[2] - 1])

    return answer

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        row = bin(arr1[i] | arr2[i])[2:].replace('1', '#').replace('0', ' ')

        if len(row) < n:
            space = " " * (n - len(row))
            row = space + row
        answer.append(row)
    return answer

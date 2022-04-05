def solution(numbers, target):
    parent = [0]

    for i in numbers:
        child = []

        for j in parent:
            child.append(j + i)
            child.append(j - i)
        parent = child

    return parent.count(target)

import math


def recursion_find(gene, index):
    first_gene = "Rr"

    if gene == 1:
        return first_gene

    if 0 <= index < math.pow(4, gene - 2):
        return "RR"
    elif 3 * math.pow(4, gene - 2) <= index < 4 * math.pow(4, gene - 2):
        return "rr"
    else:
        mid = (math.pow(4, gene - 2) + 3 * math.pow(4, gene - 2)) // 2

        if index < mid:
            index -= math.pow(4, gene - 2)
        else:
            index -= 2 * math.pow(4, gene - 2)

        return recursion_find(gene - 1, int(index))


def solution(queries):
    answer = []

    for gene, index in queries:
        answer.append(recursion_find(gene, index - 1))

    return answer

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):
    type_cnt = defaultdict(int)
    container_ball_cnt = []

    for i in range(len(container)):
        container_ball_cnt.append(sum(container[i]))
        for j in range(len(container[i])):
            type_cnt[j] += container[i][j]

    if sorted(container_ball_cnt) == sorted(type_cnt.values()):
        return "Possible"
    return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

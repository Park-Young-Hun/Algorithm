#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
class Participant:
    def __init__(self, score, rank):
        self.score = score
        self.rank = rank


def climbingLeaderboard(ranked, player):
    # Write your code here
    answer = []
    participants = []
    rank = 1

    for i in range(len(ranked)):
        if i > 0 and ranked[i - 1] > ranked[i]:
            rank += 1
        participants.append(Participant(ranked[i], rank))

    r_ranked = list(reversed(ranked))

    for score in player:
        insert_idx = len(ranked) - bisect_left(r_ranked, score)

        if insert_idx == 0:
            answer.append(1)
            continue

        target = participants[insert_idx - 1]

        if score < target.score:
            answer.append(target.rank + 1)
        else:
            answer.append(target.rank)

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

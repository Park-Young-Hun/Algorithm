import sys
from collections import defaultdict


def solution(w, k):
    min_val = len(w)
    max_val = -1
    chr_idx = defaultdict(list)

    for i in range(len(w)):
        chr_idx[w[i]].append(i)

    for key, arr in chr_idx.items():
        start = 0
        end = k - 1

        if len(arr) < k:
            continue

        while end < len(arr):
            length = arr[end] - arr[start] + 1
            min_val = min(min_val, length)
            max_val = max(max_val, length)
            start += 1
            end += 1

    return min_val, max_val


t = int(sys.stdin.readline())

for _ in range(t):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline())

    min_val, max_val = solution(w, k)

    if min_val == -1 or max_val == -1:
        print(-1)
    else:
        print(min_val, max_val)

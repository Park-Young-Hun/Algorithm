import sys
from collections import deque


def solution(n, arr, cmds):
    is_reverse = False
    q = deque(arr)

    for cmd in cmds:

        if cmd == "R":
            if is_reverse:
                is_reverse = False
            else:
                is_reverse = True
        elif cmd == "D":
            if not q:
                return "error"

            if is_reverse:
                q.pop()
            else:
                q.popleft()
    if is_reverse:
        q.reverse()

    return str(list(q))


t = int(sys.stdin.readline())

for _ in range(t):
    cmds = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    if arr[0] == "":
        arr = []
    else:
        arr = map(int, arr)

    print(solution(n, arr, cmds).replace(" ", ""))

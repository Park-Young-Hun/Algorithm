import sys


n, m = map(int, sys.stdin.readline().split())
never_heard = [sys.stdin.readline().rstrip() for _ in range(n)]
never_seen = [sys.stdin.readline().rstrip() for _ in range(m)]
never_heard_seen = []

never_heard_set = set(never_heard)

for name in never_seen:
    if name in never_heard_set:
        never_heard_seen.append(name)

never_heard_seen.sort()

print(len(never_heard_seen))

for name in never_heard_seen:
    print(name)

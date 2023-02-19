import sys

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    command = sys.stdin.readline().split()  # 최대 300만 라인의 입력이 들어오기 때문에 나눠서 입력을 받아야함.

    if len(command) == 1:
        if command[0] == "all":
            s = {i+1 for i in range(20)}
        else:
            s.clear()
    else:
        cmd = command[0]
        target = int(command[1])

        if cmd == "add":
            s.add(target)
        elif cmd == "remove":
            s.discard(target)
        elif cmd == "toggle":
            if target in s:
                s.remove(target)
            else:
                s.add(target)
        else:
            if target in s:
                print(1)
            else:
                print(0)

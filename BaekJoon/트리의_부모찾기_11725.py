import sys
from collections import defaultdict
from collections import deque

n = int(sys.stdin.readline())

tree = defaultdict(list)

for _ in range(n - 1):
    edge = sys.stdin.readline().split()
    tree[edge[0]].append(edge[1])
    tree[edge[1]].append(edge[0])

queue = deque('1')
visited = [0] * n
visited[0] = 1
result = {str(i + 1): 0 for i in range(n)}

while queue:
    now = queue.popleft()
    for i in tree[now]:
        if visited[int(i) - 1] == 0:
            result[i] = now
            visited[int(i) - 1] = 1
            queue.append(i)

for key in result.keys():
    if key != '1':
        print(result[key])

import sys
input = sys.stdin.readline
from collections import deque
n, m, v = map(int, input().split())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(n+1):
    arr[i].sort()

visited_1 = [False]*(n+1)

result_1 = []
def dfs(start):
    visited_1[start] = True
    print(start, end=' ')
    for i in arr[start]:
        if not visited_1[i]:
            dfs(i)

dfs(v)
print()

visited = [False]*(n+1)
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for value in arr[q]:
            if not visited[value]:
                visited[value] = True
                queue.append(value)

bfs(v)

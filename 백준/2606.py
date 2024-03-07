import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
k = int(input())

g = [[] for _ in range(n+1)]
chk = [False] * (n+1)

for i in range(1, k+1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

result = 0
def bfs(graph, start, visited):
    global result
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                result+=1

bfs(g, 1, chk)

print(result)


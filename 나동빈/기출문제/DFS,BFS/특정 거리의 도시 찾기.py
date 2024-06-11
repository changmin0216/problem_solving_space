import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (n+1)

def bfs(start):
    result = []
    q = deque()
    visited[start]=True
    q.append([start, 0])

    while q:
        now, cost = q.popleft()

        if cost == k:
            result.append(now)
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append([i, cost+1])

    return result
result=bfs(x)

if not result:
    print(-1)
else:
    result.sort()
    print('\n'.join(map(str, result)))

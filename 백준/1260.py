from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def bfs(start):
    q = deque()
    q.append(start)

    visited = [False] * (n+1)
    visited[start] = True

    while q:
        e = q.popleft()
        print(e, end=' ')
        for i in graph[e]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return

def dfs(start):
    print(start, end = ' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
    return

visited = [False] * (n + 1)
dfs(v)
print()
bfs(v)
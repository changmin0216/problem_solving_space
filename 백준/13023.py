import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False]*n

def dfs(depth, idx):
    if depth == 4:
        print(1)
        exit()

    for v in arr[idx]:
        if not visited[v]:
            visited[v] = True
            dfs(depth+1, v)
            visited[v] = False

for i in range(n):
    if not visited[i]:
        visited[i] = True
        dfs(0, i)
        visited[i] = False
print(0)
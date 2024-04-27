import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(y, x, k):

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 > ny or ny >= n or 0 > nx or nx >= n:
            continue

        if visited[ny][nx] == True:
            continue

        if graph[ny][nx]<=k:
            continue

        visited[ny][nx] = True
        dfs(ny, nx, k)
    return

max = 0
for k in range(0, 101):
    result = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j]>k and visited[i][j]==False:
                visited[i][j]=True
                dfs(i, j, k)
                result+=1
    if max < result:
        max = result
print(max)
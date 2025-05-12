import sys
input = sys.stdin.readline

dy = [1,-1,0,0]
dx = [0,0,-1,1]
def dfs(y, x, h):
    visited[y][x] = True

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0<=ny<n and 0<=nx<n:
            if not visited[ny][nx] and graph[ny][nx] < h:
                dfs(y, x, h)

def solution(h):
    result = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph < h:
                dfs(i, j, h)
                result+=1

    return result

########################
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

min_num = sys.maxsize
max_num = -1

for i in graph:
    min_ = min(i)
    max_ = max(i)

    if min_ < min_num:
        min_num = min_

    if max_ > max_num:
        max_num = max_


for h in (min_num, max_num+1):
    visited = [[False] * n for _ in range(n)]
    solution(h)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map_ = []
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(n):
    map_.append(list(map(int, input().rstrip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def dfs_recursive(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<n and 0<=nx<m and visited[ny][nx] == False:
            if map_[ny][nx] == 0:
                visited[ny][nx] = True
                dfs_recursive(ny, nx)
    return

result = 0
for i in range(n):
    for j in range(m):
        if map_[i][j] == 0 and visited[i][j]==False:
            visited[i][j] = True
            dfs_recursive(i, j)
            result+=1

print(result)



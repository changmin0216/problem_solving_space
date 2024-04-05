import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

maps = []

for _ in range(n):
    maps.append(list(map(int, input().rstrip())))

visited = [[False for _ in range(m)] for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(y, x):
    q = deque()
    visited[y][x] = True
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]
            if 0<=ny<n and 0<=nx<m:
                if not visited[ny][nx] and maps[ny][nx] ==1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    maps[ny][nx] = maps[ey][ex]+1

bfs(0, 0)
print(maps[n-1][m-1])
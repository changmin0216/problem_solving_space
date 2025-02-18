import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

## 각 영역의 개수를 세고
## 가장 많은 영역에서 내가 만든 로직을 돌리면??
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def bfs(p1, p2):
    q = deque()
    q.append((p1[0], p1[1], 0))

    visited = [[False]*m for _ in range(n)]
    visited[p1[0]][p1[1]] = True

    while q:
        ey, ex, dist = q.popleft()

        if ey == p2[0] and ex == p2[1]:
            return dist
        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                if map_[ny][nx] == 'L':
                    visited[ny][nx] = True
                    q.append((ny, nx, dist + 1))
    return -1

n, m = map(int, input().split())

map_ = []
for _ in range(n):
    map_.append(list(input().rstrip()))

ground = []
for i in range(n):
    for j in range(m):
        if map_[i][j] == 'L':
            ground.append((i, j))

result = -1
for c in combinations(ground, 2):
    v = bfs(c[0], c[1])
    if v != -1:
        result = max(result, v)
print(result)
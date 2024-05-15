import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

map_ = []
for _ in range(n):
    map_.append(list(map(int, input().rstrip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

q = deque()
q.append((0,0))

while q:
    ey, ex = q.popleft()

    for i in range(4):
        ny = ey + dy[i]
        nx = ex + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue

        if map_[ny][nx] == 0:
            continue

        if map_[ny][nx] == 1:
            map_[ny][nx] = map_[ey][ex]+1
            q.append((ny, nx))

print(map_[n-1][m-1])
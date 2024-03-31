import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
maps = []
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    maps.append(list(map(int, input().rstrip())))

def bfs(y, x):
    cnt=1
    q = deque()
    q.append((y, x))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while q:
        ey, ex = q.popleft()
        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt+=1
    return cnt

result=0
sum = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            sum.append(bfs(i, j))
            result+=1
print(result)
sum.sort()
for v in sum:
    print(v)
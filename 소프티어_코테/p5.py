import sys
from collections import deque
input = sys.stdin.readline

s = list(map(int, input().split()))
if len(s)!=2:
    print(-1)
    exit()

for v in s:
    if v <= 1:
        print(-1)
        exit()

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

visited = [[-1 for _ in range(s[1])] for _ in range(s[0])]

def bfs(y, x):
    q = deque()
    q.append((0,0))

    visited[y][x]+=1

    while q:
        y, x = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<s[0] and 0<=nx<s[1]:
                if visited[ny][nx]==-1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

    return

bfs(0,0)

for i in range(s[0]):
    for j in range(s[1]):
        if visited[i][j]==-1:
            print('F', end='')
            print(max(map(max, visited)))
            exit()

print('T', end='')
print(max(map(max, visited)))
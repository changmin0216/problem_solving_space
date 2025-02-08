import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dy = [-1,1,0,0]
dx = [0,0,-1,1]
def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        ey, ex = q.popleft()

        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]

            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 1
                    q.append((ny, nx))

answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(i, j)
            answer+=1
print(answer)


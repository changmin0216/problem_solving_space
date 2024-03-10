import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

maps = []
chk = [[False for _ in range(N)] for _ in range(N)]
y, x = 0, 0
for i in range(N):
    l = list(map(int, input().split()))
    if 9 in l:
        y, x = i, l.index(9) #아기 상어의 위치
    maps.append(l)

##더 이상 먹을 수 있는 물고기가 없으면 종료

shark_size = 2 #아기 상어의 크기

#상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        ey, ex = q.popleft()
        if 0 < maps[ey][ex] < shark_size: #내가 먹을 수 있는 곳
            maps[ey][ex] = 0

        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]

            if 0<=ny<N and 0<=nx<N and chk[ny][nx]==False:
                if shark_size >= [ny][nx]: ##빈칸 or 같은 사이즈의 물고기 or 먹을 수 있는 물고기
                    q.append((ny, nx))
                    chk[ny][nx] = True





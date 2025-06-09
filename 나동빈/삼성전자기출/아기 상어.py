from collections import deque

N = int(input())

fish = []
shark_size = 2
shark_y, shark_x = 0,0
eating_cnt = 0

graph = []
for i in range(N):
    list_ = list(map(int, input().split()))
    for j in range(N):
        if list_[j]!=0:
            if list_[j] == 9:
                shark_y, shark_x = i, j
                list_[j] = 0 ## 아기 상어 원래 위치 0으로

            else:
                fish.append((i, j, list_[j]))

    graph.append(list_)

# 상 좌 우 하
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]
def bfs():
    global shark_size, shark_y, shark_x, eating_cnt

    q = deque()
    q.append((shark_y, shark_x, 0))

    visited = [[False]*N for _ in range(N)]
    visited[shark_y][shark_x] = True

    candidate = []
    while q:
        ey, ex, time = q.popleft()

        if 0<graph[ey][ex]<shark_size:
            candidate.append((ey, ex, time))

        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]

            if 0<=ny<N and 0<=nx<N:
                if not visited[ny][nx]:
                    if graph[ny][nx] <= shark_size: ##나 보다 작거나 같은 경우 통과 가능
                        visited[ny][nx] = True
                        q.append((ny, nx, time+1))

    if not candidate:
        return -1

    candidate.sort(key = lambda x:(x[2], x[0], x[1]))

    y, x, time = candidate[0]

    eating_cnt+=1
    if eating_cnt == shark_size:
        shark_size += 1
        eating_cnt = 0

    shark_y, shark_x = y, x

    fish.remove((y,x,graph[y][x]))

    graph[y][x] = 0

    return time

def check():
    if len(fish) == 0:
        return False

    for i in range(len(fish)):
        if fish[i][2]<shark_size:
            return True

    return False

cnt = 0
while check():
    time_ = bfs()
    if time_==-1:
        break
    cnt+=time_
print(cnt)
from collections import deque

def flattening():
    # 동
    for i in range(m, m * 2):
        for j in range(m * 2, m * 3):
            flat_wall[i][j] = wall[0][i - m][j - (m * 2)]
    # 서
    for i in range(m, m * 2):
        for j in range(0, m):
            flat_wall[i][j] = wall[1][i - m][j]

    # 남
    for i in range(m * 2, m * 3):
        for j in range(m, m * 2):
            flat_wall[i][j] = wall[2][i - (m * 2)][j - m]

    # 북
    for i in range(m):
        for j in range(m, m * 2):
            flat_wall[i][j] = wall[3][i][j - m]

    # 윗면
    for i in range(m, m * 2):
        for j in range(m, m * 2):
            flat_wall[i][j] = wall[4][i - m][j - m]

n, m, f = map(int, input().split())

space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

# 동, 서, 남, 북, 윗면
# wall = [[] for _ in range(5)]
wall = []
for k in range(5):
    tmp = []
    for _ in range(m):
        tmp.append(list(map(int, input().split())))

    t = [[-1]*m for _ in range(m)]
    if k==0: ## 동쪽
        for i in range(m):
            for j in range(m):
                t[m-1-j][i] = tmp[i][j]
        wall.append(t)

    elif k==1: ## 서쪽
        for i in range(m):
            for j in range(m):
                t[j][m-1-i] = tmp[i][j]
        wall.append(t)
    elif k==2: ## 남쪽
        wall.append(tmp)
    elif k==3: ## 북쪽
        for i in range(m):
            for j in range(m):
                t[m-1-i][m-1-j] = tmp[i][j]
        wall.append(t)
    else:
        wall.append(tmp)

anomaly = []
for _ in range(f):
    tmp = list(map(int, input().split()))
    anomaly.append(tmp)

flat_wall = [[-1]*(m*3) for _ in range(m*3)]
flattening() #평탄화

t_y, t_x = 0, 0
flag = False
for i in range(n):
    for j in range(n):
        if space[i][j] == 3:
            t_y, t_x = i, j ##2, 2
            flag = True
            break
    if flag:
        break

## 시간의 벽 탈출구 표시(5)
s_y, s_x = -1, 1
for i in range(t_y-1, t_y+m+1): ## 1, 6
    for j in range(t_x-1, t_x+m+1): ## 1, 6
        if space[i][j] == 0:
            s_y, s_x = i, j
            if i==t_y-1: # 북쪽
                flat_wall[0][j - t_x + m] = 5
            elif i==t_y+m: ## 남쪽
                flat_wall[m*3-1][j - t_x + m] = 5
            elif j==t_x-1: ## 서쪽
                flat_wall[i - t_y + m][0] = 5
            else: ## 동쪽
                flat_wall[i - t_y + m][m*3-1] = 5

# 동, 서, 남, 북
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

## 언제 면 이동이 필요할까?
## 가려는 공간이 -1일때 (범위 밖은 못 감)
## 가려는 공간이 -1이면 이제 내가 어느 면인지 확인해서 좌표를 옮겨줘야 함
## 현재 내가 어느 위치인지 알려주는 함수

def now_pos(y, x):
    # 동쪽
    ## y값의 범위는 3~5, x값의 범위는 6~8
    if m<=y<m*2 and m*2<=x<m*3:
        return 0

    # 서쪽
    ## y값의 범위는 3~5, x값의 범위는 0~2
    elif m<=y<m*2 and 0<=x<m:
        return 1

    # 남쪽
    ## y값의 범위는 6~8, x값의 범위는 3~5
    elif m*2<=y<m*3 and m<=x<m*2:
        return 2

    # 북쪽
    else:
        return 3

def move_wall(y, x):
    now_wall = now_pos(y, x)
    if now_wall == 0: # 현재 위치가 동쪽이면
        if y == m: ## 북쪽으로
            return (m*3-1) - x , m*2-1
        else: ## 남쪽으로
            return x, y

    elif now_wall == 1: # 현재 위치가 서쪽이면
        if y == m: ## 북쪽으로
            return x, y
        else: ## 남쪽으로
            return (m*3-1) - x, m

    elif now_wall == 2: # 현재 위치가 남쪽이면
        if x == m: ## 서쪽으로
            return m*2-1, (m*3-1)-y
        else: ## 동쪽으로
            return x, y

    else: # 현재 위치가 북쪽이면
        if x == m: ## 서쪽으로
           return x, y
        else: ## 동쪽으로
            return m, (m*3-1) - y

## 이제 탈출구로 이동
def escape_time_wall():
    ## 시작 위치
    sy, sx = 0, 0
    for i in range(m, m*2):
        for j in range(m, m*2):
            if flat_wall[i][j] == 2:
                sy, sx = i, j
    # print(sy, sx)
    q = deque()
    q.append((sy, sx, 0))

    visited = [[False] * (m*3) for _ in range(m*3)]
    visited[sy][sx] = True

    while q:
        ey, ex, dist = q.popleft()

        if flat_wall[ey][ex] == 5:
            return dist
        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]

            if 0<=ny<m*3 and 0<=nx<m*3: ##범위 안에
                if flat_wall[ny][nx] == -1: ##벽을 넘어야 할 때
                    ny, nx = move_wall(ey, ex)
                if flat_wall[ny][nx]!=1 and not visited[ny][nx]:
                    visited[ny][nx]=True
                    q.append((ny, nx, dist+1))
time = escape_time_wall()

for i in range(len(anomaly)):
    r, c, d, v = anomaly[i]
    space[r][c] = 1

for i in range(1, time+1):

    for j in range(len(anomaly)):
        r, c, d, v = anomaly[j]

        if r==-1: ## 얘는 더 이상 의미X
            continue

        if i%v==0:
            nr, nc = r + dy[d]*(i//v), c + dx[d]*(i//v)

            if 0<=nr<n and 0<=nc<n:

                if space[nr][nc] == 0: ## 0이면
                    space[nr][nc] = 1 ## 확산

                else: ## 더이상 확산 X
                    anomaly[j][0] = -1

if space[s_y][s_x] == 1: ## 만약 탈출구에 이상 현상이 확산되었다면
    print(-1)
    exit()

for i in range(n):
    for j in range(n):
        if space[i][j] == 4:
            target_y, target_x = i, j
            break

def bfs():
    global time

    time+=1 ## 이제 평면에서 시작

    ##bfs로 최단거리 탑색
    q = deque()
    q.append((s_y, s_x, time))

    visited = [[False]*n for _ in range(n)]

    while q:
        ey, ex, dist = q.popleft()

        for i in range(len(anomaly)):
            r, c, d, v = anomaly[i]
            if r==-1:
                continue
            if dist%v == 0:
                nr, nc = r + dy[d] * (dist // v), c + dx[d] * (dist // v)
                if 0 <= nr < n and 0 <= nc < n:

                    if space[nr][nc] == 0:  ## 0이면
                        space[nr][nc] = 1  ## 확산
                        anomaly[i][-1] += v
                    else:  ## 더이상 확산 X
                        anomaly[i][0] = -1

        if space[ey][ex] == 1: ## 만약 이미 확산 되었다면
            continue

        visited[ey][ex] = True

        if ey==target_y and ex==target_x:
            return dist

        for i in range(4):
            ny, nx = ey + dy[i], ex + dx[i]

            if 0<=ny<n and 0<=nx<n:
                if space[ny][nx]!=1 and not visited[ny][nx]:
                    q.append((ny, nx, dist+1))
    return -1

# 13
result = bfs()
print(result)
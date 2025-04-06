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
wall = [[] for _ in range(5)]
for i in range(5):
    for _ in range(m):
        wall[i].append(list(map(int, input().split())))

anomaly = []
for _ in range(f):
    anomaly.append(list(map(int, input().split())))

flat_wall = [[-1]*(m*3) for _ in range(m*3)]
flattening() #평탄화

t_y, t_x = 0, 0
for i in range(n):
    for j in range(n):
        if space[i][j] == 3:
            t_y, t_x = i, j ##2, 2
            break

## 시간의 벽 탈출구 표시(5)
for i in range(t_y-1, t_y+m+1): ## 1, 6
    for j in range(t_x-1, t_x+m+1): ## 1, 6
        if space[i][j] == 0:
            if i==t_y-1: # 북쪽
                flat_wall[0][j - t_x + m] = 5
            elif i==t_y+m: ## 남쪽
                flat_wall[m*3-1][j - t_x + m] = 5
            elif j==t_x-1: ## 서쪽
                flat_wall[i - t_y + m][0] = 5
            else: ## 동쪽
                flat_wall[i - t_y + m][m*3-1] = 5

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

def mpve_wall(y, x):
    now_wall = now_pos(y, x)
    if now_wall == 0: # 현재 위치가 동쪽이면
        if y == m: ## 북쪽으로
            return (m*3-1) - x , m*2-1
        else: ## 남쪽으로
            return x, y

    elif now_wall == 1: # 현재 위치가 서쪽이면
        if y == m: ## 북쪽으로
            return (m-1) - x, m
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

## 시작 위치
sy, sx = 0, 0
for i in range(m, m*2):
    for j in range(m, m*2):
        if flat_wall[i][j] == 2:
            sy, sx = i, j

q = deque((sy, sx))
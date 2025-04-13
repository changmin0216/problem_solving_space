##################
n, m, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shark_d = list(map(int, input().split()))

d = [[] for _ in range(m)]
for i in range(m):
    for _ in range(4):
        d[i].append(list(map(int, input().split())))

v = [[[0,0]] * n for _ in range(n)]

shark = [] ## [i, j, num, d]
for i in range(n):
    for j in range(n):
        if graph[i][j]!=0:
            shark.append([i, j, graph[i][j], shark_d[graph[i][j]-1]])

## [1] 상어 이동
for s_y, s_x, num, d in shark:
    move
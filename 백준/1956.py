import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

min_ = int(1e9)

for i in range(1, v+1):
    if graph[i][i] < min_:
        min_ = graph[i][i]

if min_ != int(1e9):
    print(min_)
else:
    print(-1)
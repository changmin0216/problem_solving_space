import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i==j:
            graph[i][j] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a-1][b-1] = min(cost, graph[a-1][b-1])

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

distance = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    distance[a][b] = 1
    distance[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

dist = distance[1][k] + distance[k][x]

if dist >= INF:
    print("-1")
else:
    print(dist)
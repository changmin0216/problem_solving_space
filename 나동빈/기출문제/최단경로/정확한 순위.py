import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

ary = []

g = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    g[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if g[i][j] != INF or g[j][i] != INF:
            count+=1
    if count == n:
        result+=1
print(result)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]

g = []
for _ in range(n):
    g.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + g[i-1][j-1]

print(dp[n][m])
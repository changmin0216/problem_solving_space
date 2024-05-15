import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [-1] * (10001)

coin = []
for _ in range(n):
    coin.append(int(input()))

for v in coin:
    dp[v] = 1

for i in range(1, m+1):
    min = sys.maxsize
    for v in coin:
        if dp[i-v]!=-1:
            if dp[i-v]+1 < min:
                min = dp[i-v]+1
                dp[i] = min
print(dp[m])
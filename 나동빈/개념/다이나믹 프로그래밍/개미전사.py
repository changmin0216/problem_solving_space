import sys
input = sys.stdin.readline

n = int(input())
eat = list(map(int, input().split()))

dp = [0]*n
dp[0] = eat[0]
dp[1] = max(eat[0], eat[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + eat[i])

print(dp[n-1])

import sys
input = sys.stdin.readline

n = int(input())
ary = []
for _ in range(n):
    ary.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+ary[i][0], n+1):
        if dp[j] < dp[i] + ary[i][1]:
            dp[j] = dp[i] + ary[i][1]
print(dp[-1])
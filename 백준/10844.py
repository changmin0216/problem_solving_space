import sys
input = sys.stdin.readline

n = int(input())

dp = [[0]*10 for _ in range(n+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]  #끝자리가 0인 경우는 이전 거 끝자리가 1인 거랑 똑같음
        elif j == 9:
            dp[i][j] = dp[i-1][8] #끝자리가 9인 경우는 이전 거 끝자리가 8인 거랑 똑같음
        else:
            dp[i][j] = dp[i-1][j+1] + dp[i-1][j-1]

print(sum(dp[n])%(10**9))
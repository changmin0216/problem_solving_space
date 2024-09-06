import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    ary = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(ary[index:index+m])
        index+=m
    for j in range(1, m):
        for i in range(n):
            if i==0:
                dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i + 1][j - 1])
            elif i==n-1:
                dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i - 1][j - 1])
            else:
                dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i - 1][j - 1], dp[i + 1][j - 1])
    max_num = -1
    for i in range(n):
        if max_num < dp[i][-1]:
            max_num = dp[i][-1]
    print(max_num)
import sys
input = sys.stdin.readline

## 3킬로그램과 5킬로그램
## 3 ≤ N ≤ 5000

n = int(input())

if n<=5:
    if n==4:
        print(-1)
    else:
        print(1)
else:
    dp = [-1] * (n+1)
    dp[3] = 1
    dp[5] = 1

    for i in range(6, n+1):
        if dp[i-3] == -1 and dp[i-5] == -1:
            continue
        if dp[i-3] != -1 and dp[i-5] != -1:
            dp[i] = min(dp[i-3], dp[i-5]) + 1
        elif dp[i-3] == -1:
            dp[i] = dp[i-5] + 1
        else:
            dp[i] = dp[i-3] + 1
    print(dp[n])

# n = int(input())
#
# answer = 0
#
# while n>=0:
#     if n%5 == 0:
#         answer+=n//5
#         print(answer)
#         break
#     n-=3
#     answer+=1
# else:
#     print(-1)
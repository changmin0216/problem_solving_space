import sys
input = sys.stdin.readline

# t = int(input())
#
# for _ in range(t):
#     n = int(input())
#     if n<=2:
#         print(n)
#     else:
#         dp = [0] * (n+1)
#         dp[1] = 1
#         dp[2] = 2
#         dp[3] = 4
#         for i in range(4,n+1):
#             dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
#
#         print(dp[n])

def go(sum, goal):
    if sum > goal:
        return
    elif sum == goal:
        global answer
        answer+=1
        return

    for i in range(1, 4):
        go(sum+i, goal)

t = int(input())

answer = 0
for _ in range(t):
    n = int(input())
    go(0, n)
    print(answer)
    answer=0
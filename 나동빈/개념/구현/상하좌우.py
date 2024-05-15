import sys
input = sys.stdin.readline

# n = int(input())
# com = list(map(str, input().split()))
#
# x, y = 1, 1
#
# for i in range(len(com)):
#     if (com[i]=='R' and x<n):
#         x+=1
#     elif (com[i]=='L' and x>1):
#         x-=1
#     elif (com[i]=='U' and y>1):
#         y-=1
#     elif (com[i]=='D' and y<n):
#         y+=1;
#     else:
#         continue
# print(y, x)

n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)
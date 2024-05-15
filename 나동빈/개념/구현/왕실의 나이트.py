import sys
input = sys.stdin.readline

pos = input()

x = ord(pos[0]) - (ord('a')-1)
y = int(pos[1])

# 1. x=2 y=1, x=2 y=-1, x=-2 y=1, x=-2 y=-1
# 2, x=1 y=2, x=1 y=-2, x=-1 y=2, x=-1 y=-2

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

cnt = 0
for i in range(8):
    ny = y+dy[i]
    nx = x+dx[i]

    if (nx<1 or nx>8 or ny<1 or ny>8):
        continue
    cnt+=1
print(cnt)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]

now = list(map(int, input().split()))
map = [list(map(int, input().split())) for _ in range(n)]

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

x = now[1]
y = now[0]
d = now[2]

cnt = 0
while(1):
    flag = False
    for i in range(4): #4가지 방향 모두 검색
        d = (d + 3)%4

        nx = x + directions[d][0]
        ny = y + directions[d][1]

        if 0 <= nx < m and 0 <= ny <= n:
            if(not visited[ny][nx] and map[ny][nx]==0):
                visited[ny][nx] = True
                x = nx
                y = ny
                cnt+=1
                flag = True
                break
    if not flag: # 4방향 모두 돌았지만 갈 곳이 없다
        nx = x - directions[d][0]
        ny = y - directions[d][1]

        if 0<=nx<=m and 0<=ny<=n and map[ny][nx]==0:
            x = nx
            y = ny
        else:
            break
print(cnt)
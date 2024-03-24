import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

result = 0
for i in range(n):
    for j in range(m):

        if j+3<m: # 파랑이
            temp = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i][j+3]
            result = max(result, temp)


        if i+3<n: #파랑이
            temp = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+3][j]
            result = max(result, temp)

        if j+1<m and i+1<n: # 2x2
            temp = maps[i][j] + maps[i+1][j] + maps[i][j+1] + maps[i+1][j+1]
            result = max(result, temp)


        if i+2<n and j+1<m: #주황색, 초록색
            temp1_1 = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+2][j+1]
            temp1_2 = maps[i+2][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+2][j+1]

            temp1_3 = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i][j+1]
            temp1_4 = maps[i][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+2][j+1]

            temp2_1 = maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+2][j+1]
            temp2_2 = maps[i][j+1] + maps[i+1][j] + maps[i+1][j+1] + maps[i+2][j]

            temp_3 = maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 1][j + 1]
            temp_4 = maps[i + 1][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j + 1]

            result = max(result, temp1_1, temp1_2, temp1_3, temp1_4, temp2_1, temp2_2, temp_3, temp_4)

        if i+1<n and j+2<m:
            temp1_5 = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j]
            temp1_6 = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+2]

            temp1_7 = maps[i][j] + maps[i+1][j] + maps[i+1][j+1] + maps[i+1][j+2]
            temp1_8 = maps[i][j+2] + maps[i+1][j] + maps[i+1][j+1] + maps[i+1][j+2]

            temp2_3 = maps[i][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i+1][j+2]
            temp2_4 = maps[i+1][j] + maps[i][j+1] + maps[i+1][j+1] + maps[i][j+2]

            temp_1 = maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 1]
            temp_2 = maps[i][j + 1] + maps[i + 1][j] + maps[i+1][j + 1] + maps[i + 1][j + 2]

            result = max(result, temp1_5, temp1_6, temp1_7, temp1_8, temp2_3, temp2_4, temp_1, temp_2)

print(result)

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
# visited = [[False for _ in range(m)] for _ in range(n)]
# result = 0
# def dfs(y, x, g, cnt):
#     global result
#     if cnt == 4:
#         result = max(result, g)
#         return
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
#             visited[ny][nx] = True
#             dfs(ny, nx, g + maps[ny][nx], cnt+1)
#             visited[ny][nx] = False
#
# def fuck(y, x):
#     global result
#     tmp = maps[y][x]
#     arr = []
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
#             arr.append(maps[ny][nx])
#     if len(arr)==4:
#         arr.sort(reverse=True)
#         arr.pop()
#         result = max(result, sum(arr)+tmp)
#     elif len(arr)==3:
#         result = max(result, sum(arr)+tmp)
#     return
# for i in range(n):
#     for j in range(m):
#         if visited[i][j] == False:
#             visited[i][j] = True
#             dfs(i, j, maps[i][j], 1)
#             fuck(i, j)
#             visited[i][j] = False
# print(result)
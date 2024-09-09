import sys
# from collections import deque
import heapq
input = sys.stdin.readline
INF = int(1e9)

t = int(input())

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for _ in range(t):
    n = int(input())
    g = []
    for _ in range(n):
        g.append(list(map(int, input().split())))

    q = [(g[0][0], 0, 0)]
    distance = [[INF] * n for _ in range(n)]

    while q:
        dist, y, x = heapq.heappop(q)

        if distance[y][x] < dist:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                cost = dist + g[ny][nx]
                if cost < distance[ny][nx]:
                    distance[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))
    print(distance[n-1][n-1])


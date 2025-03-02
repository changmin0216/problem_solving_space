import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dy = [-1,1,0,0]
dx = [0,0,-1,1]
def find_short_path(graph, N):
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = graph[0][0]

    q = []
    heapq.heappush(q, (0,0,distance[0][0]))

    while q:
        y, x, dist = heapq.heappop(q)

        if distance[y][x] < dist:
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0<=ny<N and 0<=nx<N:
                cost = dist + graph[ny][nx]
                if distance[ny][nx] > cost:
                    distance[ny][nx] = cost
                    heapq.heappush(q, (ny, nx, cost))
    return distance[N-1][N-1]


T = int(input())

for _ in range(T):
    N = int(input())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    print(find_short_path(graph, N))
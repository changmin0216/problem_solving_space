import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start_node = int(input())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    st, end, cost = map(int, input().split())
    graph[st].append([end, cost])

INF = 1e8
distance = [INF for _ in range(v+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

dijkstra(start_node)

for i in range(1, len(distance)):
    if distance[i] == 1e8:
        print('INF', end=' ')
    else:
        print(distance[i], end=' ')
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return

n, d = map(int, input().split())

graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

#일단 거리 1로 초기화.
for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    st, end, cost = map(int, input().split())

    ## 지름길이 고속도로 거리 보다 길때
    if end-st < cost:
        continue

    ## 지름길 범위가 고속도로 밖일때
    if end > d:
        continue

    graph[st].append([end, cost])

dijkstra(0)
print(distance[d])

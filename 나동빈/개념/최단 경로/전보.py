import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

distance = [INF] * (n+1)
def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

cnt = 0
sum_ = 0
for i in range(1, n+1):
    if distance[i] != INF and distance[i]!=0:
        cnt+=1

print(cnt, max(distance[1::]))
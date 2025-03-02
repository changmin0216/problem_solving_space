import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n+1)

distance[1] = 0

q = []
heapq.heappush(q, (1, 0))

while q:
    now, dist = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(q, (i[0], cost))

max_ = -1
for i in range(1, n+1):
    if distance[i]!=INF:
        if distance[i] > max_:
            max_ = distance[i]
print(distance.index(max_), max_, distance.count(max_))
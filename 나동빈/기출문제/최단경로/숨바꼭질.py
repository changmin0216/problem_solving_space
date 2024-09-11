import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF for _ in range(n+1)]

distance[1] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,1))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + 1

            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
dijkstra(1)

max = 0
max_index = -1
for i in range(1, n+1):
    if max < distance[i]:
        max = distance[i]
        max_index = i
print(max_index, distance[max_index], distance.count(distance[max_index]))
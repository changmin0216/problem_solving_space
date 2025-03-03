import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

time = []

graph = [[] for _ in range(N+1)]

indegree = [0] * (N+1)

for i in range(N):
    a = list(map(int, input().split()))

    time.append(a[0]) ##각 강의의 시간

    for j in range(1, len(a)-1):
        graph[a[j]].append(i+1)
        indegree[i+1]+=1

q = deque()

for i in range(1, len(indegree)):
    if indegree[i] == 0:
        q.append((i, time[i-1]))

while q:
    now, t, = q.popleft()
    print(t)
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append((i, time[i-1]+t))
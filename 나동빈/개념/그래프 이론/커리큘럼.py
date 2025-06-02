import sys, copy
from collections import deque
input = sys.stdin.readline

n = int(input())

indegree = [0] * (n+1)

graph = [[] for _ in range(n+1)]
time = [0]
for k in range(n):
    tmp = list(map(int, input().split()))
    time.append(tmp[0])
    for i in range(1, len(tmp)-1):
        indegree[k+1]+=1
        graph[tmp[i]].append(k+1)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i]-=1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()
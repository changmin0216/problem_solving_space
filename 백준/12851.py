import sys
input = sys.stdin.readline
from collections import deque
max_size = 100001

n, k = map(int, input().split())

visited = [-1] * max_size
visited[n] = 0

cnt = 0
q = deque()
q.append(n)
while q:
    x = q.popleft()

    if x == k:
        cnt+=1
    for nx in [x-1, x+1, x*2]:
        if 0<=nx<max_size and (visited[nx]==-1 or visited[nx]>=visited[x]+1):
            visited[nx] = visited[x]+1
            q.append(nx)

print(visited[k])
print(cnt)
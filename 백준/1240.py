import sys

input = sys.stdin.readline
N, M = map(int, input().split())
graph = list([0] * (N + 1) for _ in range(N + 1))
answer = 0


def dfs(s, e, dist):
    global answer
    visited[s] = 1
    for i in range(1, N + 1):
        if graph[s][i] > 0 and not visited[i]:
            if i == e:
                answer = dist + graph[s][i]
            else:
                dfs(i, e, dist + graph[s][i])


for i in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for i in range(M):
    a, b = map(int, input().split())
    visited = [0] * (N + 1)
    dfs(a, b, 0)
    print(answer)
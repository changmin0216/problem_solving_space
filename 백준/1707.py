import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(k, colors):
    color[k] = colors ## 내 노드 색깔 칠하기

    for i in g[k]:
        if not visited[i]: ## 만약 방문하지 않았다면
            visited[i] = True ## 방문하고
            a = dfs(i, -colors) ## 내 색깔과 반대의 색으로 dfs ㄱㄱ
            if not a:
                return False
        elif color[i] == color[k]: ## 이미 방문을 했는데 색깔이 같으면
            return False
    return True

k = int(input()) # 테스트 케이스 개수

for i in range(k):
    v, e = map(int, input().split()) # 정점의 개수, 간선의 개수
    g = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    visited = [0] * (v+1)
    color = [0] * (v+1)
    for i in range(1, v+1):
        if not visited[i]:
            visited[i] = True
            result = dfs(i, 1)
            if not result:
                break
    if result:
        print('YES')
    else:
        print('NO')
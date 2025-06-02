import sys
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

distance = [-1] * (n+1) ## 자기 자신을 중심으로 했을떄 원의 지름
distance[1] = 0

def dfs(start, dist):
    for i in tree[start]:
        if distance[i[0]] == -1: # 아직 방문한 곳이 아니면
            distance[i[0]] = i[1] + dist
            dfs(i[0], distance[i[0]])

dfs(1, 0) ## 1에서 부터 거리의 합
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)
#
# n = int(input())
# tree = [[] for _ in range(n+1)]
# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     tree[a].append([b, c])
#     tree[b].append([a, c])
#
# distance = [-1] * (n+1)
# distance[1] = 0
#
# def dfs(start, dist):
#     for i in tree[start]:
#         if distance[i[0]]==-1:
#             distance[i[0]] = i[1] + dist
#             dfs(i[0], distance[i[0]])
#
# dfs(1, 0)
#
# start = distance.index(max(distance))
# distance = [-1] * (n + 1)
# distance[start] = 0
# dfs(start, 0)
#
# print(max(distance))
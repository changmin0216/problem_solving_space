import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
parent = [0] * n
for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(n):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i, j)

result = True
for i in range(m-1):
    if find_parent(parent, plan[i]-1) != find_parent(parent, plan[i+1]-1):
        result = False

if result:
    print('YES')
else:
    print('False')
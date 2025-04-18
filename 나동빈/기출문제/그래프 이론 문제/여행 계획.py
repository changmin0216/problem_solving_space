import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    com = list(map(int, input().split()))

    for j in range(n):
        if com[j] == 1:
            if find_parent(parent, i+1)!= find_parent(parent, j+1):
                union_parent(parent, i+1, j+1)

journey = list(map(int, input().split()))

result = parent[journey[0]]
for i in range(1, m):
    if parent[journey[i]]!=result:
        print("NO")
        break
else:
    print("YES")
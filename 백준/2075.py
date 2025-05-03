import sys
input = sys.stdin.readline

## 1<=n<=1500
n = int(input())

l = []

graph = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

    for i in tmp:
        l.append(i)

l.sort()
print(l[-n])

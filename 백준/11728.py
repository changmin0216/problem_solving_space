import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = list(map(int, input().split())) # 3, 5
b = list(map(int, input().split())) # 2, 9

s, e = 0, 0

result = []
while s<n and e<m:
    if a[s] < b[e]:
        result.append(a[s])
        s+=1
    else:
        result.append(b[e])
        e+=1

if s==n:
    result.extend(b[e:])
else:
    result.extend(a[s:])

print(' '.join(map(str, result)))
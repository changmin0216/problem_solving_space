import sys
input = sys.stdin.readline

n, m  = map(int, input().split())

bowling = list(map(int, input().split()))

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if bowling[i]!=bowling[j]:
            cnt+=1
print(cnt)
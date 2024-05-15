import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0
while(1):
    if n%k == 0:
        n = n//k
    else:
        n = n-1
    cnt+=1
    if(n == 1):
        break
print(cnt)



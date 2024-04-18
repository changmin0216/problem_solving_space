import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
ary = list(map(int, input().split()))
ary.sort()

answer = 0
while(1):
    for _ in range(k):
        if m==0:
            break
        answer+=ary[-1]
        m-=1
    if m==0:
        break
    answer+=ary[-2]
    m-=1
print(answer)
import sys
input = sys.stdin.readline

n = int(input())
fear = list(map(int, input().split()))

fear.sort()

result = 0
cnt = 0
for v in fear:
    cnt+=1
    if cnt == v:
        result+=1
        count=0

print(result)
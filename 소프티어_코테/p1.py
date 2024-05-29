import sys
from itertools import permutations
input = sys.stdin.readline

l = list(map(str, input().split()))

if len(l) > 9:
    print(-1)
    exit()

if 7<=len(l)<=9:
    for c in l:
        if len(c) > 2 or len(c)==0:
            print(-1)
            exit()

if len(l)<=6:
    for c in l:
        if len(c) > 3 or len(c)==0:
            print(-1)
            exit()
if len(l)==0:
    print(-1)
    exit()

result = []
for c in permutations(l, len(l)):
    temp = ''
    for i in range(len(l)):
        temp += c[i]
    result.append(int(temp))

print(max(result)+min(result))

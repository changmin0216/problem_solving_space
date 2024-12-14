## t<=20
## n<=100,000

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: x[0])
    max = arr[0][1]
    result = 1
    for i in range(n):
        if arr[i][1] < max:
            max = arr[i][1]
            result+=1
    print(result)
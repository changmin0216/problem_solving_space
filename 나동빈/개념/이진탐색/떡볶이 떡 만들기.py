import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))

left = 0
right = max(rice_cake)

result=0
while left <= right:
    mid = (left+right) // 2

    sum=0
    for i in range(n):
        if rice_cake[i] > mid:
            sum+=rice_cake[i] - mid

    if sum < m:
        right = mid - 1
    else:
        result = mid
        left = mid + 1
print(result)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = max(arr)
answer = -1
while left<=right:
    mid = (left + right) // 2

    sum_ = 0
    for i in arr:
        h = i - mid
        if h>0:
            sum_+=h

    if sum_>=m:
        answer = mid
        left = mid + 1
    else: ## sum_<m
        right = mid - 1

print(answer)
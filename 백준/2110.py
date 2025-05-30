import sys
input = sys.stdin.readline

n, c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

start = 0
end = arr[-1] - arr[0]

answer = 0
while start<=end:
    mid = (start + end) // 2

    cnt = 1
    value = arr[0]
    for i in range(1, n):
        if arr[i] >= value + mid:
            cnt+=1
            value = arr[i]

    if cnt<c:
        end = mid-1
    else: ##cnt>=c
        answer = mid
        start = mid+1

print(answer)
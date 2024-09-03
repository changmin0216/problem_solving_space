import sys
input = sys.stdin.readline

N, C = map(int, input().split())

home = []
for i in range(N):
    home.append(int(input()))
home.sort()

start = 1
end = home[-1] - home[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    value = home[0]
    count = 1

    for i in range(1, N):
        if home[i] >= value + mid:
            value = home[i]
            count+=1

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)
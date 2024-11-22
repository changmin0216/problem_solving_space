import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(input().rstrip())

## 길이를 기준으로 정렬
arr.sort(key=lambda x:len(x))

answer = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j][0:len(arr[i])]:
            break
    else:
        answer+=1

print(answer)
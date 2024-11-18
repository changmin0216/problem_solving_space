import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))

answer = -1
for i in range(n):
    cnt = 0
    for j in range(n):
        if i==j:
            continue
        if arr[i][j] == 'Y':
            cnt+=1
        else:
            for k in range(n):
                if arr[j][k] == 'Y' and arr[i][k] == 'Y':
                    cnt+=1
                    break
    answer = max(answer, cnt)

print(answer)
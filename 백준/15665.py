import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
temp = []
def recur():
    if len(temp)==m:
        print(*temp)
        return
    prev = 0
    for i in range(n):
        if prev!=arr[i]:
            temp.append(arr[i])
            prev = arr[i]
            recur()
            temp.pop()
recur()
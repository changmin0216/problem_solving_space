import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    tree = list(map(int, input().split()))

    tree.sort()

    left = 0
    right = n-1
    normal = [0] * n
    for i in range(n):
        if i%2==0:
            normal[left] = tree[i]
            left+=1
        else:
            normal[right] = tree[i]
            right-=1

    answer = 0
    for i in range(n-1):
        answer = max(answer, abs(normal[i]-normal[i+1]))

    print(answer)
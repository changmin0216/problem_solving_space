import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []
for i in range(n):
    temp = list(map(int, input().split()))
    answer.append(min(temp))
answer.sort()
print(answer[-1])


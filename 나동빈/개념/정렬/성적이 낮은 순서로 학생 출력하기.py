import sys
input = sys.stdin.readline

n = int(input())

ary = []
for _ in range(n):
    ary.append(list(input().split()))

ary.sort(key=lambda x: int(x[1]))

for student in ary:
    print(student[0], end=' ')
import sys
input = sys.stdin.readline

n = int(input())

ary = []
for _ in range(n):
    ary.append(int(input()))
print(sorted(ary, reverse=True))
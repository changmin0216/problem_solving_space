import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    c = {}
    for _ in range(n):
        name, category = map(str, input().rstrip())
        c[category] = name
    print(c)

import sys
input = sys.stdin.readline

n = int(input())

tozi = []
for _ in range(n):
    tozi.append(list(map(str, input().split())))

disable = [[0 for _ in range(n)] for _ in range(n)]

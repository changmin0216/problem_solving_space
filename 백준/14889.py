import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())

arr = []
result = sys.maxsize
for _ in range(n):
    arr.append(list(map(int, input().split())))

person = [i for i in range(n)]

team = []
for v in combinations(person, n//2):
    team.append(v)

for i in range(len(team)//2):
    start=0
    link=0
    for q in combinations(team[i], 2):
        start+=arr[q[0]][q[1]]+arr[q[1]][q[0]]

    for w in combinations(team[-(i+1)], 2):
        link+=arr[w[0]][w[1]]+arr[w[1]][w[0]]

    result = min(abs(start-link), result)

print(result)
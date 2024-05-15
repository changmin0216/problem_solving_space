import sys
input = sys.stdin.readline

n = int(input())
part_num = set(map(int, input().split()))

m = int(input())
part_find = list(map(int, input().split()))

for i in range(m):
    if part_find[i] in part_num:
        print('yes', end=' ')
    else:
        print('no', end=' ')

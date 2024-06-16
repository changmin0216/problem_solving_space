### pypy에서만 돌아감
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

op_r = []
for i in range(4):

    if i==0:
        for _ in range(op[i]):
            op_r.append('+')

    elif i==1: 
        for _ in range(op[i]):
            op_r.append('-')

    elif i==2:
        for _ in range(op[i]):
            op_r.append('*')

    else:
        for _ in range(op[i]):
            op_r.append('/')

result = []
for l in permutations(op_r, len(op_r)):
    tmp = arr[0]
    for i in range(n-1):
        if l[i] == '+':
            tmp+=arr[i+1]
        elif l[i] == '-':
            tmp-=arr[i+1]
        elif l[i] == '*':
            tmp*=arr[i+1]
        else:
            if tmp<0 and arr[i+1]>0:
                tmp = -(-tmp//arr[i+1])
            else:
                tmp = tmp//arr[i+1]
    result.append(tmp)

print(max(result))
print(min(result))


### 백트래킹(Python3로도 돌아감 효율 굳굳)
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# nums = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
# result = []
# ans = 0
# def cal(add, sub, mul, div, ans, i):
#     if i == n:
#         result.append(ans)
#         return
#     if add>0:
#         cal(add-1, sub, mul, div, ans+nums[i], i+1)
#     if sub>0:
#         cal(add, sub-1, mul, div, ans-nums[i], i+1)
#     if mul>0:
#         cal(add, sub, mul-1, div, ans*nums[i], i+1)
#     if div>0:
#         cal(add, sub, mul, div-1, int(ans/nums[i]), i+1)
# cal(add, sub, mul, div,  nums[0], 1)
# print(max(result))
# print(min(result))